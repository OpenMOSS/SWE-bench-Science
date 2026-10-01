from __future__ import annotations

import asyncio
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import AsyncMock, patch

from pier.environments.agent_setup import squid_bootstrap_command
from pier.environments.base import ExecResult
from pier.environments.docker.docker import DockerEnvironment
from pier.models.agent.network import NetworkAllowlist
from pier.models.task.config import EnvironmentConfig
from pier.models.trial.paths import TrialPaths

from scripts.pier_network import (
    ISOLATED_OPTION,
    ScienceBenchDocker,
    assert_container_capabilities,
    assert_isolated_network,
    gateway_endpoints,
    gateway_proxy_script,
)
from scripts.run_batch import inference_urls, job_error_count, main


class NetworkPolicyTests(unittest.TestCase):
    def test_failed_trial_is_not_a_successful_batch(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "result.json"
            path.write_text(json.dumps({"stats": {"n_errored_trials": 1}}))
            self.assertEqual(job_error_count(path), 1)
            path.write_text(json.dumps({"stats": {"n_errored_trials": 0}}))
            self.assertEqual(job_error_count(path), 0)

    def make_environment(self, directory: str, domains: list[str] | None = None):
        root = Path(directory)
        environment_dir = root / "environment"
        environment_dir.mkdir(exist_ok=True)
        (environment_dir / "Dockerfile").write_text("FROM python:3.11-slim\n")
        trial_dir = root / "trial"
        trial_dir.mkdir(exist_ok=True)
        return ScienceBenchDocker(
            environment_dir=environment_dir,
            environment_name="network-test",
            session_id="network-test",
            trial_paths=TrialPaths(trial_dir=trial_dir),
            task_env_config=EnvironmentConfig(docker_image="python:3.11-slim", allow_internet=False),
            network_allowlist=NetworkAllowlist(domains=domains or []),
            inference_urls=["http://192.0.2.10:4000/v1"],
        )

    def test_gateway_port_is_bound_to_configured_host(self):
        script = gateway_proxy_script(squid_bootstrap_command(), gateway_endpoints(["http://192.0.2.10:4000/v1"]))
        self.assertIn("gateway_0_host dst 192.0.2.10/32", script)
        self.assertIn("gateway_0_port port 4000", script)
        self.assertIn("http_access allow authenticated gateway_0_host gateway_0_port", script)
        self.assertIn("http_access allow authenticated allowed_domains standard_ports", script)
        self.assertIn("acl SSL_ports port 443\n", script)
        self.assertNotIn("http_access allow authenticated allowed_domains\n", script)

    def test_https_gateway_uses_nonstandard_connect_port(self):
        script = gateway_proxy_script(squid_bootstrap_command(), gateway_endpoints(["https://gateway.example:8443/v1"]))
        self.assertIn("acl SSL_ports port 443 8443", script)
        self.assertIn("gateway_0_host dstdomain gateway.example", script)
        self.assertIn("http_access deny all", script)

    def test_gateway_values_reject_injection_and_unsupported_protocols(self):
        for value in ("file:///tmp/key", "http://gateway.example%0Aevil:4000", "http://x:99999"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                gateway_endpoints([value])

    def test_gateway_metadata_never_contains_url_credentials(self):
        urls = inference_urls("codex", {"CODEX_BASE_URL": "http://user:password@gateway.example:4000/v1?key=secret"}, [])
        self.assertEqual(urls, ["http://gateway.example:4000"])

    def test_claude_gateway_and_explicit_codex_config_ports_are_supported(self):
        self.assertEqual(inference_urls("claude-code", {"ANTHROPIC_BASE_URL": "https://gateway.example:8443"}, []), ["https://gateway.example:8443"])
        config = '[model_providers.custom]\nbase_url="http://192.0.2.10:4000/v1"\n'
        self.assertEqual(inference_urls("codex", {}, ["config_toml=" + config]), ["http://192.0.2.10:4000"])

    def test_generated_compose_isolates_main_and_disables_proxy_forwarding(self):
        with tempfile.TemporaryDirectory() as directory:
            env = self.make_environment(directory, ["192.0.2.10"])
            env._prepare_egress_proxy_compose()
            proxy_config = json.loads(env._egress_proxy_compose_path.read_text())
            internal = proxy_config["networks"]["pier-egress-internal"]
            self.assertTrue(internal["internal"])
            self.assertFalse(internal["enable_ipv6"])
            self.assertEqual(internal["driver_opts"][ISOLATED_OPTION], "isolated")
            self.assertEqual(proxy_config["services"]["main"]["networks"], ["pier-egress-internal"])
            proxy = proxy_config["services"]["pier-egress-proxy"]
            self.assertEqual(proxy["sysctls"]["net.ipv4.ip_forward"], "0")
            self.assertEqual(proxy["sysctls"]["net.ipv6.conf.all.forwarding"], "0")
            self.assertIn("NET_RAW", proxy["cap_drop"])
            hardening = json.loads(env._docker_compose_paths[-1].read_text())
            self.assertIn("NET_RAW", hardening["services"]["main"]["cap_drop"])

    def test_unallowlisted_gateway_does_not_gain_custom_port_access(self):
        with tempfile.TemporaryDirectory() as directory:
            env = self.make_environment(directory, ["api.allowed.test"])
            env._prepare_egress_proxy_compose()
            script = (env.trial_paths.trial_dir / "egress-proxy/start-squid.sh").read_text()
            self.assertNotIn("4000", script)

    def test_no_inference_environment_keeps_network_none(self):
        with tempfile.TemporaryDirectory() as directory:
            env = self.make_environment(directory)
            env._prepare_egress_proxy_compose()
            self.assertIsNone(env._egress_proxy_compose_path)
            self.assertIn(env._DOCKER_COMPOSE_NO_NETWORK_PATH, env._docker_compose_paths)

    def test_network_inspection_rejects_gateway_and_ignored_options(self):
        good = {"Driver": "bridge", "Internal": True, "EnableIPv6": False,
                "Options": {ISOLATED_OPTION: "isolated"}, "IPAM": {"Config": [{"Subnet": "172.30.0.0/24"}]}}
        assert_isolated_network(good)
        for bad in ({**good, "Internal": False}, {**good, "Options": {}},
                    {**good, "EnableIPv6": True},
                    {**good, "IPAM": {"Config": [{"Gateway": "172.30.0.1"}]}}):
            with self.assertRaises(RuntimeError):
                assert_isolated_network(bad)

    def test_privileged_or_added_capabilities_are_rejected(self):
        good = {"HostConfig": {"CapDrop": ["NET_ADMIN", "NET_RAW"]}}
        assert_container_capabilities(good)
        assert_container_capabilities({"HostConfig": {"CapDrop": ["CAP_NET_ADMIN", "CAP_NET_RAW"]}})
        for host in ({"CapDrop": []}, {**good["HostConfig"], "Privileged": True},
                     {**good["HostConfig"], "CapAdd": ["NET_RAW"]}):
            with self.assertRaises(RuntimeError):
                assert_container_capabilities({"HostConfig": host})

    def test_extra_agent_network_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            env = self.make_environment(directory, ["192.0.2.10"])
            env._prepare_egress_proxy_compose()
            container = {"HostConfig": {"CapDrop": ["NET_ADMIN", "NET_RAW"]},
                         "NetworkSettings": {"Networks": {"internal": {}, "default": {}}}}
            with (patch.object(env, "_run_docker_compose_command", new=AsyncMock(return_value=ExecResult(stdout="main-id", return_code=0))),
                  patch.object(env, "_docker_inspect", new=AsyncMock(return_value=container))):
                with self.assertRaisesRegex(RuntimeError, "exclusively"):
                    asyncio.run(env._validate_running_network())

    def test_failed_isolation_check_cleans_up_before_agent_runs(self):
        with tempfile.TemporaryDirectory() as directory:
            env = self.make_environment(directory)
            with (patch.object(DockerEnvironment, "start", new=AsyncMock()),
                  patch.object(env, "_validate_running_network", new=AsyncMock(side_effect=RuntimeError("invalid network"))),
                  patch.object(env, "stop", new=AsyncMock()) as stop):
                with self.assertRaisesRegex(RuntimeError, "invalid network"):
                    asyncio.run(env.start(False))
                stop.assert_awaited_once_with(delete=False)

    def test_batch_runner_always_selects_shared_network_adapter(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "task_002"
            root.mkdir()
            (root / "pre_artifacts.sh").write_text("#!/bin/sh\n")
            (root / "task.toml").write_text('[environment]\ndocker_image="env:test"\n[verifier.environment]\ndocker_image="verifier:test"\n')
            args = ["run_batch.py", "--path", str(root), "--agent", "claude-code", "--skip-pull", "--dry-run"]
            with patch.object(sys, "argv", args), patch("scripts.run_batch.pier_version", return_value="0.3.0"), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(), 0)
            record = json.loads((root / "batch-run.json").read_text())
            self.assertEqual(record["network_policy"], "internal-isolated-squid-v1")
            self.assertIn("scripts.pier_network:ScienceBenchDocker", record["pier_command"])

    def test_codex_import_path_does_not_get_shadowed_by_builtin_agent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "task_002"
            root.mkdir()
            (root / "pre_artifacts.sh").write_text("#!/bin/sh\n")
            (root / "task.toml").write_text('[environment]\ndocker_image="env:test"\n[verifier.environment]\ndocker_image="verifier:test"\n')
            args = ["run_batch.py", "--path", str(root), "--agent", "codex", "--skip-pull", "--dry-run"]
            with patch.object(sys, "argv", args), patch("scripts.run_batch.pier_version", return_value="0.3.0"), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(main(), 0)
            record = json.loads((root / "batch-run.json").read_text())
            self.assertIn("--agent-import-path scripts.pier_adapters:ScienceBenchCodex", record["pier_command"])
            self.assertNotIn("--agent codex", record["pier_command"])


if __name__ == "__main__":
    unittest.main()
