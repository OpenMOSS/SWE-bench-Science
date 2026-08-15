from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.generate_huggingface import GPL_IDS, load_rows, write_selection
from scripts.import_task import base_image_for, dependency_lines, normalize_task_id
from scripts.materialize import (
    expand_task_selectors,
    normalize_task_id as normalize_materialized_task_id,
    task_source,
)
from scripts.provider_config import render_codex_config, resolve_codex_profile
from scripts.run_batch import pier_version, redacted_command, task_dirs
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
        self.assertEqual(summary["gpl_family"], 12)
        rows = load_rows()
        self.assertEqual(sum(bool(row.get("gpl_family")) for row in rows), len(GPL_IDS))
        self.assertEqual(
            {str(row["release_id"]) for row in rows if bool(row.get("gpl_family"))},
            GPL_IDS,
        )

    def test_selection_writer_is_explicit_and_does_not_add_aliases(self) -> None:
        rows = [row for row in load_rows() if str(row["release_id"]) in {"001", "002"}]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "selection.json"
            write_selection(rows, path)
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["task_ids"], ["001", "002"])
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

    def test_dependency_extractor_ignores_python_stdlib_names(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory)
            (source / "requirements.txt").write_text(
                "collections\nfunctools\nitertools\nnumpy>=2\n",
                encoding="utf-8",
            )
            self.assertEqual(dependency_lines(source, task_id="034", language="python"), ["numpy>=2", "pytest==8.3.5"])

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

    def test_batch_runner_accepts_single_task_and_redacts_agent_env(self) -> None:
        root = Path(__file__).resolve().parents[1] / "tasks" / "task_002"
        self.assertEqual(task_dirs(root), [root])
        rendered = redacted_command(["pier", "run", "--agent-env", "TOKEN=secret"])
        self.assertNotIn("TOKEN=secret", rendered)
        self.assertIn("<redacted>", rendered)
        rendered_kwarg = redacted_command(["pier", "run", "--agent-kwarg", "api_token=secret"])
        self.assertNotIn("api_token=secret", rendered_kwarg)
        self.assertIn("api_token=<redacted>", rendered_kwarg)

    def test_batch_runner_reads_pier_version_without_failing_missing_binary(self) -> None:
        self.assertIsNone(pier_version("/path/that/does/not/exist"))

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
