from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.build_publish_batch import smoke_verifier
from scripts.generate_huggingface import gpl_ids, load_rows, restricted_ids, write_selection
from scripts.import_task import (
    base_image_for,
    classify_license_text,
    dependency_lines,
    detect_license,
    normalize_task_id,
    render_system_package_lines,
    runtime_config,
)
from scripts.materialize import (
    expand_task_selectors,
    normalize_task_id as normalize_materialized_task_id,
    task_source,
)
from scripts.material_policy import load_policies
from scripts.provider_config import render_codex_config, resolve_codex_profile
from scripts.publish_material_updates import requires_clean_rebuild
from scripts.run_batch import (
    pier_version,
    redacted_command,
    task_dirs,
    validate_artifact_hooks,
)
from scripts.summarize_results import write_summary
from scripts.validate_release import validate


class ReleaseToolTests(unittest.TestCase):
    def test_release_ids_are_zero_padded_and_legacy_id_is_rejected(self) -> None:
        self.assertEqual(normalize_task_id("1"), "001")
        self.assertEqual(normalize_task_id("task_019"), "019")
        with self.assertRaises(ValueError):
            normalize_task_id("120")

    def test_manifest_has_119_rows_and_exact_gpl_gate(self) -> None:
        summary = validate(require_images=False)
        self.assertEqual(summary["rows"], 119)
        self.assertEqual(summary["gpl_family"], 18)
        rows = load_rows()
        self.assertEqual(summary["restricted_license"], len(restricted_ids(rows)))
        self.assertEqual(summary["unrestricted"], 119 - len(restricted_ids(rows)))
        gpl_gate_ids = {
            str(row["release_id"])
            for row in rows
            if bool(row.get("gpl_family"))
        }
        self.assertEqual(gpl_gate_ids, gpl_ids(rows))
        self.assertTrue(gpl_gate_ids)
        self.assertEqual(sum(bool(row.get("gpl_family")) for row in rows), len(gpl_ids(rows)))
        self.assertTrue(gpl_ids(rows) <= restricted_ids(rows))
        self.assertTrue({"019", "026", "101", "102"} <= restricted_ids(rows))

    def test_091_105_material_policies_are_complete(self) -> None:
        policies = load_policies()
        expected = {f"{task_id:03d}" for task_id in range(91, 106)}
        self.assertTrue(expected.issubset(policies))
        gated = {
            task_id
            for task_id in expected
            if bool(policies[task_id].get("requires_restricted_gate"))
        }
        self.assertEqual(gated, {"096", "097", "098", "100", "101", "102"})
        required_fields = {
            "path", "source_url", "license", "copyright", "modified",
            "third_party_exceptions", "distribution_decision",
        }
        for task_id in expected:
            self.assertTrue(policies[task_id]["materials"])
            for material in policies[task_id]["materials"]:
                self.assertTrue(required_fields.issubset(material), (task_id, material))
                self.assertIn(
                    material["distribution_decision"],
                    {"bundled", "restricted", "excluded"},
                )

    def test_031_045_material_policies_are_complete_and_gates_are_explicit(self) -> None:
        policies = load_policies()
        expected = {f"{task_id:03d}" for task_id in range(31, 46)}
        self.assertTrue(expected.issubset(policies))
        self.assertEqual(
            {
                task_id
                for task_id in expected
                if bool(policies[task_id].get("requires_restricted_gate"))
            },
            {"032", "035"},
        )
        required_fields = {
            "path", "source_url", "license", "copyright", "modified",
            "third_party_exceptions", "distribution_decision",
        }
        for task_id in expected:
            materials = policies[task_id]["materials"]
            self.assertGreater(len(materials), 0)
            for material in materials:
                self.assertTrue(required_fields.issubset(material), (task_id, material))
                self.assertIn(
                    material["distribution_decision"],
                    {"bundled", "restricted", "excluded"},
                )
        self.assertEqual(
            {
                task_id for task_id in expected
                if requires_clean_rebuild(policies[task_id])
            },
            {"032", "033", "037", "038", "039", "041", "045"},
        )
        self.assertIn(
            "environment/public/paper_assets/openmm_article.html",
            policies["032"]["remove"],
        )
        self.assertTrue(
            any(
                material["path"]
                == "environment/public/paper_assets/openmm_article.html"
                and material["distribution_decision"] == "excluded"
                for material in policies["032"]["materials"]
            )
        )

    def test_046_060_material_policies_capture_remediation(self) -> None:
        policies = load_policies()
        expected = {f"{task_id:03d}" for task_id in range(46, 61)}
        self.assertTrue(expected.issubset(policies))
        self.assertEqual(
            {
                task_id
                for task_id in expected
                if bool(policies[task_id].get("requires_restricted_gate"))
            },
            {"057"},
        )
        required_fields = {
            "path", "source_url", "license", "copyright", "modified",
            "third_party_exceptions", "distribution_decision",
        }
        excluded_paths: set[str] = set()
        for task_id in expected:
            materials = policies[task_id]["materials"]
            self.assertGreater(len(materials), 0)
            for material in materials:
                self.assertTrue(required_fields.issubset(material), (task_id, material))
                self.assertIn(
                    material["distribution_decision"],
                    {"bundled", "restricted", "excluded"},
                )
                if material["distribution_decision"] == "excluded":
                    excluded_paths.add(str(material["path"]))
        self.assertTrue(
            {
                "environment/public/paper_assets/vaughan_nowak_1997 and "
                "environment/public/paper_assets/ingram_2019",
                "environment/public/paper_assets/fig1.png, fig2.png, and fig3.png",
                "environment/public/paper_assets/leo-perturbations.png",
            }.issubset(excluded_paths)
        )

    def test_selection_writer_is_explicit_and_does_not_add_aliases(self) -> None:
        rows = [row for row in load_rows() if str(row["release_id"]) in {"001", "002"}]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selection.json"
            write_selection(rows, path)
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["task_ids"], ["001", "002"])
            self.assertFalse(payload["allow_restricted_licenses"])
            self.assertNotIn("allow_gpl", payload)
            self.assertNotIn("120", payload["task_ids"])

    def test_materializer_rejects_legacy_id(self) -> None:
        self.assertEqual(normalize_materialized_task_id("2"), "002")
        with self.assertRaises(ValueError):
            normalize_materialized_task_id("120")

    def test_materializer_expands_lists_and_ranges(self) -> None:
        self.assertEqual(
            expand_task_selectors(["002,005-007", "009"]),
            {"002", "005", "006", "007", "009"},
        )
        with self.assertRaises(ValueError):
            expand_task_selectors(["007-005"])

    def test_materializer_default_is_unrestricted_and_explicit_restricted_requires_gate(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "default"
            subprocess.run(
                [
                    "python3", str(root / "scripts" / "materialize.py"),
                    "--output", str(output),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            selection = json.loads((output / "selection.json").read_text(encoding="utf-8"))
            rows = load_rows()
            self.assertEqual(len(selection["task_ids"]), len(rows) - len(restricted_ids(rows)))
            self.assertFalse(selection["allow_restricted_licenses"])
            self.assertNotIn("allow_gpl", selection)
            explicit = subprocess.run(
                [
                    "python3", str(root / "scripts" / "materialize.py"),
                    "--task-id", "002,019", "--output", str(Path(directory) / "restricted"),
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(explicit.returncode, 0)
            self.assertIn("requires --allow-restricted-licenses: 019", explicit.stderr)
            gpl = subprocess.run(
                [
                    "python3", str(root / "scripts" / "materialize.py"),
                    "--task-id", "003", "--output", str(Path(directory) / "gpl"),
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(gpl.returncode, 0)
            self.assertIn("requires --allow-restricted-licenses: 003", gpl.stderr)
            legacy_flag = subprocess.run(
                [
                    "python3", str(root / "scripts" / "materialize.py"),
                    "--allow-GPL", "--output", str(Path(directory) / "legacy"),
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(legacy_flag.returncode, 0)
            self.assertIn("unrecognized arguments: --allow-GPL", legacy_flag.stderr)
            with_restricted = Path(directory) / "with_restricted"
            subprocess.run(
                [
                    "python3", str(root / "scripts" / "materialize.py"),
                    "--allow-restricted-licenses", "--output", str(with_restricted),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            with_restricted_selection = json.loads(
                (with_restricted / "selection.json").read_text(encoding="utf-8")
            )
            self.assertEqual(len(with_restricted_selection["task_ids"]), 119)
            self.assertTrue(with_restricted_selection["allow_restricted_licenses"])
            self.assertNotIn("allow_gpl", with_restricted_selection)

    def test_result_summary_flattens_trial_reward_and_failure(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            jobs = Path(directory) / "jobs"
            trial = jobs / "job-1" / "task_002__trial-a" / "verifier"
            trial.mkdir(parents=True)
            (jobs / "job-1" / "result.json").write_text(
                json.dumps(
                    {
                        "stats": {
                            "evals": {
                                "codex": {
                                    "exception_stats": {
                                        "AgentTimeoutError": ["task_002__trial-a"]
                                    }
                                }
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            (trial / "reward.json").write_text(
                json.dumps(
                    {
                        "reward": 0.0,
                        "public": {"passed": 1, "collected": 1},
                        "private": {"passed": 0, "collected": 1},
                    }
                ),
                encoding="utf-8",
            )
            summary_json, summary_csv = write_summary(jobs)
            payload = json.loads(summary_json.read_text(encoding="utf-8"))
            self.assertEqual(payload["trial_count"], 1)
            self.assertEqual(payload["rows"][0]["failure_class"], "AgentTimeoutError")
            self.assertIn("task_id,trial_id", summary_csv.read_text(encoding="utf-8"))

    def test_materializer_falls_back_to_committed_hf_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            snapshot = root / "huggingface" / "tasks" / "task_002"
            snapshot.mkdir(parents=True)
            self.assertEqual(task_source("tasks/task_002", root=root), snapshot)

    def test_pre_artifacts_hook_captures_empty_and_modified_workspaces(self) -> None:
        root = Path(__file__).resolve().parents[1]
        hook = root / "templates" / "task" / "pre_artifacts.sh"
        with tempfile.TemporaryDirectory() as directory:
            workdir = Path(directory) / "task"
            artifacts = Path(directory) / "artifacts"
            workdir.mkdir()
            subprocess.run(["git", "init", "-q"], cwd=workdir, check=True)
            subprocess.run(
                ["git", "config", "user.email", "test@example.invalid"],
                cwd=workdir,
                check=True,
            )
            subprocess.run(
                ["git", "config", "user.name", "Test"], cwd=workdir, check=True
            )
            source = workdir / "source.py"
            source.write_text("baseline\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=workdir, check=True)
            subprocess.run(
                ["git", "commit", "-q", "-m", "baseline"], cwd=workdir, check=True
            )
            env = {
                **os.environ,
                "SCI_BENCH_TASK_DIR": str(workdir),
                "ENV_ARTIFACTS_PATH": str(artifacts),
            }
            subprocess.run(["sh", str(hook)], cwd=workdir, env=env, check=True)
            patch_path = artifacts / "model.patch"
            self.assertTrue(patch_path.is_file())
            self.assertEqual(patch_path.read_bytes(), b"")

            source.write_text("committed\n", encoding="utf-8")
            subprocess.run(["git", "add", "."], cwd=workdir, check=True)
            subprocess.run(
                ["git", "commit", "-q", "-m", "agent-commit"],
                cwd=workdir,
                check=True,
            )
            source.write_text("modified\n", encoding="utf-8")
            subprocess.run(["sh", str(hook)], cwd=workdir, env=env, check=True)
            patch = patch_path.read_text(encoding="utf-8")
            self.assertIn("-baseline", patch)
            self.assertIn("+modified", patch)

    def test_run_batch_rejects_task_without_artifact_hook(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            task = Path(directory) / "task_002"
            task.mkdir()
            with self.assertRaisesRegex(ValueError, "rematerialize"):
                validate_artifact_hooks([task])

    def test_verifier_entrypoint_discovers_custom_private_test_names(self) -> None:
        root = Path(__file__).resolve().parents[1]
        task_tests = root / "huggingface" / "tasks" / "task_030" / "tests"
        grader = (task_tests / "grader.py").read_text(encoding="utf-8")
        self.assertIn('"/tests/private_tests"', grader)
        self.assertNotIn("test_task_030.py", grader)
        compose = (task_tests / "docker-compose.yaml").read_text(encoding="utf-8")
        self.assertIn("target: /tests/grader.py", compose)
        dockerfile = (task_tests / "Dockerfile").read_text(encoding="utf-8")
        self.assertIn("COPY grader.py /tests/grader.py", dockerfile)

    def test_dependency_extractor_ignores_python_stdlib_names(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            (source / "requirements.txt").write_text(
                "collections\nfunctools\nitertools\nnumpy>=2\n",
                encoding="utf-8",
            )
            self.assertEqual(dependency_lines(source, task_id="034", language="python"), ["numpy>=2", "pytest==8.3.5"])

    def test_dependency_extractor_prefers_task_runtime_pins(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            public = Path(directory)
            source = public / "source"
            source.mkdir()
            (source / "requirements.txt").write_text("pytest\n", encoding="utf-8")
            (public / "task.json").write_text(
                json.dumps(
                    {
                        "environment": {
                            "runtime": {
                                "python_packages": [
                                    "numpy==1.26.4",
                                    "openmm==8.5.2",
                                    "pytest==8.3.2",
                                ]
                            }
                        }
                    }
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                dependency_lines(source, task_id="032", language="python"),
                ["numpy==1.26.4", "openmm==8.5.2", "pytest==8.3.2"],
            )
            self.assertEqual(base_image_for(source, "python"), "python:3.11-slim")

            payload = json.loads((public / "task.json").read_text(encoding="utf-8"))
            payload["environment"]["runtime"]["base_image"] = "python:3.12-slim"
            (public / "task.json").write_text(json.dumps(payload), encoding="utf-8")
            self.assertEqual(base_image_for(source, "python"), "python:3.12-slim")

    def test_dependency_parser_preserves_markers_and_python_floor(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            (source / "pyproject.toml").write_text(
                "requires-python = '>=3.12'\n"
                "dependencies = [\n"
                "  \"importlib-resources; python_version < '3.12'\",\n"
                "]\n",
                encoding="utf-8",
            )
            self.assertEqual(base_image_for(source, "python"), "python:3.12-slim")
            self.assertEqual(
                dependency_lines(source, task_id="039", language="python"),
                ["importlib-resources; python_version < '3.12'", "pytest==8.3.5"],
            )

    def test_author_runtime_declaration_drives_release_dependencies(self) -> None:
        task_data = {
            "environment": {
                "runtime": {
                    "base_image": "python:3.12-slim",
                    "python_packages": ["numpy==2.1.0", "pytest==8.3.5"],
                    "system_packages": ["libopenblas-dev"],
                }
            }
        }
        self.assertEqual(
            runtime_config(task_data),
            (
                "python:3.12-slim",
                ["numpy==2.1.0", "pytest==8.3.5"],
                ["libopenblas-dev"],
            ),
        )
        self.assertIn("libopenblas-dev", render_system_package_lines(["libopenblas-dev"]))

    def test_license_detector_prefers_the_root_project_license(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            (source / "LICENSE").write_text(
                "GNU Lesser General Public License\nVersion 3\n",
                encoding="utf-8",
            )
            nested = source / "external" / "component"
            nested.mkdir(parents=True)
            (nested / "COPYING").write_text(
                "GNU Affero General Public License\nVersion 3\n",
                encoding="utf-8",
            )
            self.assertEqual(detect_license(source), ("LGPL-3.0-family", "LICENSE"))

    def test_gpl_cross_reference_does_not_become_agpl(self) -> None:
        text = (
            "GNU GENERAL PUBLIC LICENSE\nVersion 3\n"
            + "ordinary terms " * 100
            + "GNU Affero General Public License"
        )
        self.assertEqual(classify_license_text(text), "GPL-3.0-family")

    def test_batch_runner_accepts_single_task_and_redacts_agent_env(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory) / "task_002"
            root.mkdir()
            (root / "task.toml").write_text("version = 1\n", encoding="utf-8")
            self.assertEqual(task_dirs(root), [root])
        rendered = redacted_command(["pier", "run", "--agent-env", "TOKEN=secret"])
        self.assertNotIn("TOKEN=secret", rendered)
        self.assertIn("<redacted>", rendered)
        rendered_kwarg = redacted_command(["pier", "run", "--agent-kwarg", "api_token=secret"])
        self.assertNotIn("api_token=secret", rendered_kwarg)
        self.assertIn("api_token=<redacted>", rendered_kwarg)

    def test_batch_runner_reads_pier_version_without_failing_missing_binary(self) -> None:
        self.assertIsNone(pier_version("/path/that/does/not/exist"))

    def test_verifier_smoke_accepts_a_failing_baseline_with_collected_tests(self) -> None:
        summary = {
            "reward": 0,
            "public": {"passed": 0, "collected": 1, "return_code": 1},
            "private": {"collected": 3},
        }
        completed = subprocess.CompletedProcess(
            args=["docker"], returncode=0, stdout=json.dumps(summary) + "\n"
        )
        with patch("scripts.build_publish_batch.subprocess.run", return_value=completed):
            smoke_verifier("example.invalid/verifier:test", "089")

    def test_verifier_smoke_rejects_a_public_runner_failure(self) -> None:
        summary = {
            "reward": 0,
            "public": {"passed": 0, "collected": 1, "return_code": 2},
            "private": {"collected": 3},
        }
        completed = subprocess.CompletedProcess(
            args=["docker"], returncode=0, stdout=json.dumps(summary) + "\n"
        )
        with patch("scripts.build_publish_batch.subprocess.run", return_value=completed):
            with self.assertRaisesRegex(RuntimeError, "public_return_code=2"):
                smoke_verifier("example.invalid/verifier:test", "089")

    def test_codex_gateway_profile_selects_wire_without_embedding_key(self) -> None:
        profile = resolve_codex_profile(
            {
                "MODEL": "test-model",
                "CODEX_BASE_URL": "https://gateway.example/v1?token=hidden",
                "CODEX_WIRE_API": "chat",
                "OPENAI_API_KEY": "secret-value",
            }
        )
        config = render_codex_config(profile)
        self.assertEqual(profile.model, "test-model")
        self.assertEqual(profile.wire_api, "chat")
        self.assertEqual(profile.safe_base_url, "https://gateway.example/v1")
        self.assertIn('env_key = "OPENAI_API_KEY"', config)
        self.assertNotIn("secret-value", config)


if __name__ == "__main__":
    unittest.main()
