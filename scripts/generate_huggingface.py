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
SCIENCE_KNOWLEDGE_ABLATION_IDS = {
    *(f"{task_id:03d}" for task_id in range(2, 83)),
    "084", "086", "090",
    *(f"{task_id:03d}" for task_id in range(97, 102)),
    "111", "114",
}
FIELDS = [
    "task_id", "science_knowledge_ablation", "title", "domain", "language", "repository_url", "base_commit",
    "source_license", "gpl_family", "restricted_license", "license_gate",
    "material_license", "material_license_source", "material_restricted", "materials_gate",
    "materials_manifest_sha256", "material_licenses", "materials_provenance",
    "restricted_reason",
    "environment_image", "verifier_image", "image_platform", "task_path", "status",
]
THIN_TASK_FILES = (
    "task.toml",
    "pre_artifacts.sh",
    "instruction.md",
    "metadata.json",
    "environment/Dockerfile",
    "tests/Dockerfile",
    "tests/test.sh",
)
OPTIONAL_THIN_TASK_FILES = (
    "environment/public/MATERIALS.json",
    "environment/public/MATERIALS_LICENSES.md",
    "fixtures/PROVENANCE.md",
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


def science_knowledge_ablation(row: dict[str, object]) -> bool:
    value = row.get("science_knowledge_ablation")
    if value is not None:
        return bool(value)
    return str(row.get("release_id", "")) in SCIENCE_KNOWLEDGE_ABLATION_IDS


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            values = {field: row.get(field, "") for field in FIELDS}
            values["task_id"] = row["release_id"]
            values["science_knowledge_ablation"] = science_knowledge_ablation(row)
            values["material_licenses"] = json.dumps(
                row.get("material_licenses", []), separators=(",", ":")
            )
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
        f"Science-knowledge ablation rows: **{sum(science_knowledge_ablation(row) for row in rows)}**.",
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
        "science_knowledge_ablation": science_knowledge_ablation(row),
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
        "material_license": row.get("material_license", ""),
        "material_license_source": row.get("material_license_source", ""),
        "material_restricted": bool(row.get("material_restricted")),
        "materials_gate": bool(row.get("materials_gate")),
        "materials_manifest_sha256": row.get("materials_manifest_sha256", ""),
        "material_licenses": row.get("material_licenses", []),
        "materials_provenance": row.get("materials_provenance", ""),
        "restricted_reason": row.get("restricted_reason", ""),
        "public_payload_sha256": row.get("public_payload_sha256", ""),
    }


def write_snapshot(
    rows: list[dict[str, object]],
    output_root: Path,
    *,
    replace_task_ids: set[str] | None = None,
) -> None:
    task_root = output_root / "tasks"
    # Keep previously committed optional provenance files when the imported
    # authoring tree does not carry them. Every canonical task below is still
    # overwritten file-by-file, while this preserves audited release notices.
    for row in rows:
        task_id = str(row["release_id"])
        if replace_task_ids is not None and task_id not in replace_task_ids:
            continue
        imported_source = ROOT / str(row["task_path"])
        committed_source = task_root / Path(str(row["task_path"])).name
        source = (
            imported_source
            if (imported_source / "task.toml").is_file()
            else committed_source
        )
        destination = task_root / source.name
        # Do not delete the destination: optional release-only notices may be
        # committed in the thin bundle even when they are absent from imports.
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
            if source_file.resolve() == destination_file.resolve():
                continue
            shutil.copy2(source_file, destination_file)
        for relative in OPTIONAL_THIN_TASK_FILES:
            source_file = source / relative
            if not source_file.is_file() and relative == "fixtures/PROVENANCE.md":
                source_file = source / "environment" / "public" / relative
            if not source_file.is_file():
                continue
            destination_file = destination / relative
            destination_file.parent.mkdir(parents=True, exist_ok=True)
            if source_file.resolve() == destination_file.resolve():
                continue
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
    docs_dir = output_root / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "docs" / "run-batch.md", docs_dir / "run-batch.md")
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
    if (ROOT / "NOTICE.md").is_file():
        shutil.copy2(ROOT / "NOTICE.md", output_root / "NOTICE.md")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "huggingface" / "data")
    parser.add_argument(
        "--task-id",
        action="append",
        help="Replace only this thin task snapshot; repeatable. Tables and manifests remain global.",
    )
    args = parser.parse_args()
    rows = sorted(load_rows(), key=lambda row: str(row["release_id"]))
    expected = [f"{index:03d}" for index in range(1, 120)]
    if [str(row["release_id"]) for row in rows] != expected:
        raise ValueError("manifest must contain exactly release ids 001..119")
    write_csv(rows, args.output / "tasks.csv")
    write_statistics(rows, args.output / "statistics.md")
    # The default set excludes every restricted row, including material-only
    # gates whose source code itself is permissively licensed.
    default_rows = [
        row for row in rows
        if not bool(row.get("restricted_license", row.get("gpl_family")))
    ]
    selections_dir = args.output.parent / "selections"
    if selections_dir.exists():
        shutil.rmtree(selections_dir)
    write_selection(default_rows, selections_dir / f"default-{len(default_rows)}.json")
    write_selection(rows, selections_dir / "all-119.json")
    replace_task_ids = None
    if args.task_id:
        replace_task_ids = {
            f"{int(value.removeprefix('task_')):03d}" for value in args.task_id
        }
        known_ids = {str(row["release_id"]) for row in rows}
        unknown_ids = sorted(replace_task_ids - known_ids)
        if unknown_ids:
            raise ValueError(f"unknown task ids: {', '.join(unknown_ids)}")
    write_snapshot(rows, args.output.parent, replace_task_ids=replace_task_ids)
    print(
        json.dumps(
            {
                "rows": len(rows),
                "snapshot_tasks": len(rows) if replace_task_ids is None else len(replace_task_ids),
                "output": str(args.output),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
