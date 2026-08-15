#!/usr/bin/env python3
"""Flatten Pier job outputs into a small JSON and CSV evaluation summary."""

from __future__ import annotations

import argparse
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path


TRIAL_RE = re.compile(r"^(task_\d{3})__(.+)$")
FIELDS = (
    "task_id", "trial_id", "reward", "public_passed", "public_collected",
    "private_passed", "private_collected", "failure_class", "verifier_dir",
)


def _load_json(path: Path) -> dict[str, object]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _failure_by_trial(job_result: dict[str, object]) -> dict[str, str]:
    output: dict[str, str] = {}
    stats = job_result.get("stats")
    if not isinstance(stats, dict):
        return output
    evaluations = stats.get("evals")
    if not isinstance(evaluations, dict):
        return output
    for evaluation in evaluations.values():
        if not isinstance(evaluation, dict):
            continue
        exceptions = evaluation.get("exception_stats")
        if not isinstance(exceptions, dict):
            continue
        for failure_class, trials in exceptions.items():
            if isinstance(trials, list):
                for trial in trials:
                    output[str(trial)] = str(failure_class)
    return output


def collect_rows(jobs_dir: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for job_dir in sorted(path for path in jobs_dir.iterdir() if path.is_dir()):
        job_result = _load_json(job_dir / "result.json")
        failure_by_trial = _failure_by_trial(job_result)
        for trial_dir in sorted(path for path in job_dir.iterdir() if path.is_dir()):
            match = TRIAL_RE.match(trial_dir.name)
            if not match:
                continue
            reward = _load_json(trial_dir / "verifier" / "reward.json")
            public = reward.get("public") if isinstance(reward.get("public"), dict) else {}
            private = reward.get("private") if isinstance(reward.get("private"), dict) else {}
            rows.append(
                {
                    "task_id": match.group(1).removeprefix("task_"),
                    "trial_id": trial_dir.name,
                    "reward": reward.get("reward", ""),
                    "public_passed": public.get("passed", ""),
                    "public_collected": public.get("collected", ""),
                    "private_passed": private.get("passed", ""),
                    "private_collected": private.get("collected", ""),
                    "failure_class": failure_by_trial.get(trial_dir.name, ""),
                    "verifier_dir": str(trial_dir / "verifier"),
                }
            )
    return rows


def write_summary(jobs_dir: Path, output_dir: Path | None = None) -> tuple[Path, Path]:
    jobs_dir = jobs_dir.resolve()
    output_dir = (output_dir or jobs_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    rows = collect_rows(jobs_dir)
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "jobs_dir": str(jobs_dir),
        "trial_count": len(rows),
        "rows": rows,
    }
    json_path = output_dir / "summary.json"
    csv_path = output_dir / "summary.csv"
    json_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    return json_path, csv_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs-dir", type=Path, default=Path("jobs"))
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args()
    json_path, csv_path = write_summary(args.jobs_dir, args.output_dir)
    print(json.dumps({"summary_json": str(json_path), "summary_csv": str(csv_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
