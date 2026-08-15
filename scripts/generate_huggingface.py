#!/usr/bin/env python3
"""Generate the Hugging Face table, statistics and license-gated selections."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIELDS = [
    "task_id", "title", "domain", "language", "repository_url", "base_commit",
    "source_license", "gpl_family", "restricted_license", "license_gate",
    "environment_image", "verifier_image", "image_platform", "task_path", "status",
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


def gpl_ids(rows: list[dict[str, object]]) -> set[str]:
    return {str(row["release_id"]) for row in rows if bool(row.get("gpl_family"))}


def restricted_ids(rows: list[dict[str, object]]) -> set[str]:
    return {
        str(row["release_id"])
        for row in rows
        if bool(row.get("restricted_license", row.get("gpl_family")))
    }


def license_gate(row: dict[str, object]) -> str:
    return str(row.get("license_gate", "none"))


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
                "allow_restricted_licenses": any(
                    license_gate(row) != "none" for row in rows
                ),
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
    gated_count = len(gpl_ids(rows))
    restricted_count = len(restricted_ids(rows))
    lines = [
        "# Generated Release Statistics",
        "",
        f"Canonical rows: **{len(rows)}**; default unrestricted rows: **{len(rows) - restricted_count}**; restricted-license rows: **{restricted_count}**; GPL-family rows: **{gated_count}**.",
        "",
        f"Environment image references: **{environment_count}/{len(rows)}**; verifier image references: **{verifier_count}/{len(rows)}**.",
        "",
    ]
    lines += table("Domain", Counter(str(row.get("domain", "")) for row in rows))
    lines += table("Language", Counter(str(row.get("language", "")) for row in rows))
    lines += table("Source License", Counter(str(row.get("source_license", "")) for row in rows))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def metadata_from_row(row: dict[str, object]) -> dict[str, object]:
    return {
        "task_id": str(row["release_id"]),
        "title": row.get("title", ""),
        "domain": row.get("domain", ""),
        "language": row.get("language", ""),
        "source_repository": row.get("repository_url", ""),
        "source_commit": row.get("base_commit", ""),
        "source_license": row.get("source_license", ""),
        "license_source": row.get("license_source", ""),
        "gpl_family": bool(row.get("gpl_family")),
        "restricted_license": bool(row.get("restricted_license", row.get("gpl_family"))),
        "license_gate": row.get("license_gate", "none"),
        "public_payload_sha256": row.get("public_payload_sha256", ""),
    }


def write_snapshot(rows: list[dict[str, object]], output_root: Path) -> None:
    task_root = output_root / "tasks"
    if task_root.exists():
        shutil.rmtree(task_root)
    for row in rows:
        source = ROOT / str(row["task_path"])
        destination = task_root / source.name
        for relative in THIN_TASK_FILES:
            source_file = source / relative
            if relative == "metadata.json":
                destination_file = destination / relative
                destination_file.parent.mkdir(parents=True, exist_ok=True)
                destination_file.write_text(
                    json.dumps(metadata_from_row(row), indent=2) + "\n",
                    encoding="utf-8",
                )
                continue
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
    for script in (
        "materialize.py", "provider_config.py", "pier_adapters.py", "run_batch.py",
        "summarize_results.py",
    ):
        shutil.copy2(ROOT / "scripts" / script, tools_dir / script)
    profiles_dir = output_root / "profiles"
    profiles_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(
        ROOT / "profiles" / "codex.env.example",
        profiles_dir / "codex.env.example",
    )
    shutil.copy2(ROOT / "profiles" / "claude.env.example", profiles_dir / "claude.env.example")
    shutil.copy2(
        ROOT / "profiles" / "mini-swe-agent.env.example",
        profiles_dir / "mini-swe-agent.env.example",
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
    default_rows = [row for row in rows if license_gate(row) == "none"]
    selections_dir = args.output.parent / "selections"
    if selections_dir.exists():
        shutil.rmtree(selections_dir)
    write_selection(default_rows, selections_dir / f"default-{len(default_rows)}.json")
    write_selection(rows, selections_dir / "all-119.json")
    write_snapshot(rows, args.output.parent)
    print(json.dumps({"rows": len(rows), "output": str(args.output)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
