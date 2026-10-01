"""Enforce offline task networking in Pier without changing task images."""

from __future__ import annotations

import asyncio
import ipaddress
import json
from pathlib import Path
from urllib.parse import urlsplit

from pier.environments.agent_setup import EGRESS_PROXY_SERVICE
from pier.environments.docker.docker import DockerEnvironment


NETWORK_POLICY = "internal-isolated-squid-v1"
NETWORK_CAPABILITIES = ["NET_ADMIN", "NET_RAW"]
ISOLATED_OPTION = "com.docker.network.bridge.gateway_mode_ipv4"


def gateway_endpoints(urls: list[str]) -> list[tuple[str, str, int]]:
    endpoints = set()
    for url in urls:
        parsed = urlsplit(url)
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("Inference URLs must be absolute HTTP or HTTPS URLs")
        host = parsed.hostname.lower().rstrip(".")
        if not all(char.isalnum() or char in ".-:" for char in host):
            raise ValueError("Invalid inference gateway hostname")
        port = parsed.port or (443 if parsed.scheme == "https" else 80)
        endpoints.add((parsed.scheme, host, port))
    return sorted(endpoints)


def gateway_proxy_script(script: str, endpoints: list[tuple[str, str, int]]) -> str:
    """Allow nonstandard ports only for the corresponding configured gateway."""
    extra = [(scheme, host, port) for scheme, host, port in endpoints if port not in {80, 443}]
    if not extra:
        return script
    safe_ports = " ".join(str(port) for port in sorted({80, 443, *(port for _, _, port in extra)}))
    tls_ports = " ".join(str(port) for port in sorted({443, *(port for scheme, _, port in extra if scheme == "https")}))
    script = script.replace("acl Safe_ports port 80 443", "acl Safe_ports port " + safe_ports)
    script = script.replace("acl SSL_ports port 443", "acl SSL_ports port " + tls_ports)
    rules = ["acl standard_ports port 80 443", "http_access allow authenticated allowed_domains standard_ports"]
    for index, (_, host, port) in enumerate(extra):
        try:
            address = ipaddress.ip_address(host)
        except ValueError:
            host_acl = f"dstdomain {host}"
        else:
            host_acl = f"dst {host}/{address.max_prefixlen}"
        rules.extend([
            f"acl gateway_{index}_host {host_acl}",
            f"acl gateway_{index}_port port {port}",
            f"http_access allow authenticated gateway_{index}_host gateway_{index}_port",
        ])
    original = "http_access allow authenticated allowed_domains"
    if original not in script:
        raise RuntimeError("Unsupported Pier proxy configuration; expected datacurve-pier 0.3.0")
    return script.replace(original, "\n".join(rules))


def assert_isolated_network(network: dict) -> None:
    options = network.get("Options") or {}
    addresses = (network.get("IPAM") or {}).get("Config") or []
    if not (
        network.get("Driver") == "bridge"
        and network.get("Internal") is True
        and not network.get("EnableIPv6", False)
        and options.get(ISOLATED_OPTION) == "isolated"
        and addresses
        and all(not address.get("Gateway") for address in addresses)
    ):
        raise RuntimeError("Offline Agent requires an internal bridge with an isolated gateway (Docker Engine 28+)")


def assert_container_capabilities(container: dict) -> None:
    host = container.get("HostConfig") or {}
    dropped = {name.upper().removeprefix("CAP_") for name in host.get("CapDrop") or []}
    if host.get("Privileged") or host.get("CapAdd") or not set(NETWORK_CAPABILITIES) <= dropped:
        raise RuntimeError("Offline containers must drop NET_ADMIN and NET_RAW without added capabilities")


class ScienceBenchDocker(DockerEnvironment):
    """A shared Docker environment for every Science benchmark harness."""

    def __init__(self, *args, inference_urls: list[str] | None = None, **kwargs):
        self._inference_endpoints = gateway_endpoints(inference_urls or [])
        self._isolation_compose_path: Path | None = None
        super().__init__(*args, **kwargs)

    def _prepare_egress_proxy_compose(self) -> None:
        if self.task_env_config.allow_internet:
            raise ValueError("SWE-bench Science tasks require allow_internet=false")
        super()._prepare_egress_proxy_compose()
        if self._egress_proxy_compose_path:
            path = self._egress_proxy_compose_path
            compose = json.loads(path.read_text())
            network = compose["networks"]["pier-egress-internal"]
            network.update({"driver": "bridge", "enable_ipv6": False, "driver_opts": {ISOLATED_OPTION: "isolated"}})
            proxy = compose["services"][EGRESS_PROXY_SERVICE]
            proxy.update({
                "cap_drop": NETWORK_CAPABILITIES,
                "sysctls": {"net.ipv4.ip_forward": "0", "net.ipv6.conf.all.forwarding": "0"},
            })
            path.write_text(json.dumps(compose, indent=2) + "\n")
            bootstrap = path.parent / "egress-proxy" / "start-squid.sh"
            permitted = [
                endpoint for endpoint in self._inference_endpoints
                if any(endpoint[1] == domain or (domain.startswith(".") and endpoint[1].endswith(domain))
                       for domain in self.network_allowlist.domains)
            ]
            bootstrap.write_text(gateway_proxy_script(bootstrap.read_text(), permitted))
            self._egress_proxy_env.update({
                "ALL_PROXY": self._egress_proxy_env["HTTP_PROXY"],
                "all_proxy": self._egress_proxy_env["http_proxy"],
            })
        self._isolation_compose_path = self.trial_paths.trial_dir / f"docker-compose-isolation-{self.session_id}.json"
        self._isolation_compose_path.write_text(json.dumps({"services": {"main": {"cap_drop": NETWORK_CAPABILITIES}}}, indent=2) + "\n")

    @property
    def _docker_compose_paths(self) -> list[Path]:
        paths = super()._docker_compose_paths
        if self._isolation_compose_path:
            paths.append(self._isolation_compose_path)
        return paths

    @staticmethod
    async def _docker_inspect(*args: str) -> dict:
        process = await asyncio.create_subprocess_exec(
            "docker", *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
        )
        try:
            stdout, _ = await asyncio.wait_for(process.communicate(), timeout=15)
        except asyncio.TimeoutError:
            process.kill()
            await process.communicate()
            raise RuntimeError("Timed out validating Docker network isolation") from None
        if process.returncode:
            raise RuntimeError("Docker network isolation inspection failed")
        return json.loads(stdout)[0]

    async def _validate_running_network(self) -> dict:
        result = await self._run_docker_compose_command(["ps", "--quiet", "main"])
        container_id = (result.stdout or "").strip()
        if not container_id:
            raise RuntimeError("No Agent container exists for network validation")
        main = await self._docker_inspect("container", "inspect", container_id)
        assert_container_capabilities(main)
        report = {"policy": NETWORK_POLICY, "container_id": container_id, "inference_domains": self.network_allowlist.domains}
        if not self._egress_proxy_compose_path:
            if main["HostConfig"].get("NetworkMode") != "none":
                raise RuntimeError("Offline containers without inference egress must use network_mode=none")
            report["network_mode"] = "none"
            return report
        networks = main["NetworkSettings"]["Networks"]
        if len(networks) != 1:
            raise RuntimeError("Agent must be connected exclusively to its isolated internal network")
        internal_name = next(iter(networks))
        network = await self._docker_inspect("network", "inspect", internal_name)
        assert_isolated_network(network)
        result = await self._run_docker_compose_command(["ps", "--quiet", EGRESS_PROXY_SERVICE])
        proxy = await self._docker_inspect("container", "inspect", (result.stdout or "").strip())
        assert_container_capabilities(proxy)
        proxy_networks = proxy["NetworkSettings"]["Networks"]
        sysctls = proxy["HostConfig"].get("Sysctls") or {}
        if not (len(proxy_networks) == 2 and internal_name in proxy_networks
                and sysctls.get("net.ipv4.ip_forward") == "0"
                and sysctls.get("net.ipv6.conf.all.forwarding") == "0"):
            raise RuntimeError("Inference proxy must have two networks and IP forwarding disabled")
        report.update({"network_mode": "isolated-allowlist", "internal_network": internal_name, "host_gateway": None, "proxy_forwarding": False})
        return report

    async def start(self, force_build: bool):
        try:
            await super().start(force_build)
            report = await self._validate_running_network()
            path = self.trial_paths.trial_dir / f"network-policy-{self.session_id}.json"
            path.write_text(json.dumps(report, indent=2) + "\n")
        except BaseException:
            await self.stop(delete=False)
            raise
