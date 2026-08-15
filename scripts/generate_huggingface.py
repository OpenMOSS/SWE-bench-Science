#!/usr/bin/env python3
"""Generate the Hugging Face table, statistics and GPL selections."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GPL_IDS = {"003", "021", "023", "057", "066", "074", "075", "083", "084", "085", "100", "118"}
FIELDS = [
    "task_id", "title", "domain", "language", "repository_url", "base_commit",
    "source_license", "gpl_family", "environment_image", "verifier_image",
    "image_platform", "task_path", "status",
]
THIN_TASK_FILES = (
    "task.toml",
    "instruction.md",
    "metadata.json",
    "environment/Dockerfile",
    "tests/Dockerfile",
    "tests/test.sh",
)


def load_rows() -> list[dict[str, object]]:
    return [
        json.loads(line)
        for line in (ROOT / "manifests" / "tasks.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            values = {field: row.get(field, "") for field in FIELDS}
            values["task_id"] = row["release_id"]
            writer.writerow(values)


def write_selection(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "task_ids": [str(row["release_id"]) for row in rows],
                "allow_gpl": any(bool(row.get("gpl_family")) for row in rows),
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def write_statistics(rows: list[dict[str, object]], path: Path) -> None:
    def table(title: str, values: Counter[str]) -> list[str]:
        lines = [f"### {title}", "", "| Value | Count |", "| --- | ---: |"]
        lines.extend(f"| `{key}` | {values[key]} |" for key in sorted(values))
        return lines + [""]

    environment_count = sum(bool(row.get("environment_image")) for row in rows)
    verifier_count = sum(bool(row.get("verifier_image")) for row in rows)
    lines = [
        "# Generated Release Statistics",
        "",
        f"Canonical rows: **{len(rows)}**; default non-GPL rows: **{len(rows) - len(GPL_IDS)}**; GPL-family rows: **{len(GPL_IDS)}**.",
        "",
        f"Environment image references: **{environment_count}/{len(rows)}**; verifier image references: **{verifier_count}/{len(rows)}**.",
        "",
    ]
    lines += table("Domain", Counter(str(row.get("domain", "")) for row in rows))
    lines += table("Language", Counter(str(row.get("language", "")) for row in rows))
    lines += table("Source License", Counter(str(row.get("source_license", "")) for row in rows))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def write_snapshot(rows: list[dict[str, object]], output_root: Path) -> None:
    task_root = output_root / "tasks"
    if task_root.exists():
        shutil.rmtree(task_root)
    for row in rows:
        source = ROOT / str(row["task_path"])
        destination = task_root / source.name
        for relative in THIN_TASK_FILES:
            source_file = source / relative
            if not source_file.is_file():
                raise FileNotFoundError(source_file)
            destination_file = destination / relative
            destination_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_file, destination_file)

    manifest_dir = output_root / "manifests"
    manifest_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "manifests" / "tasks.jsonl", manifest_dir / "tasks.jsonl")
    tools_dir = output_root / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)
    for script in ("materialize.py", "provider_config.py", "pier_adapters.py", "run_batch.py"):
        shutil.copy2(ROOT / "scripts" / script, tools_dir / script)
    profiles_dir = output_root / "profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        ROOT / "profiles" / "codex.env.example",
        profiles_dir / "codex.env.example",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "huggingface" / "data")
    args = parser.parse_args()
    rows = sorted(load_rows(), key=lambda row: str(row["release_id"]))
    expected = [f"{index:03d}" for index in range(1, 120)]
    if [str(row["release_id"]) for row in rows] != expected:
        raise ValueError("manifest must contain exactly release ids 001..119")
    write_csv(rows, args.output / "tasks.csv")
    write_statistics(rows, args.output / "statistics.md")
    write_selection([row for row in rows if not bool(row.get("gpl_family"))], args.output.parent / "selections" / "default-107.json")
    write_selection(rows, args.output.parent / "selections" / "all-119.json")
    write_snapshot(rows, args.output.parent)
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
