#!/usr/bin/env python3
"""Materialize an explicit local Pier task selection from the release table."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def normalize_task_id(value: str) -> str:
    raw = value.strip().removeprefix("task_")
    if not raw.isdigit() or not 1 <= int(raw) <= 119:
        raise ValueError(f"task id must be in 001..119: {value!r}")
    return f"{int(raw):03d}"


def expand_task_selectors(values: list[str] | None) -> set[str] | None:
    """Expand repeated, comma-separated ids and inclusive id ranges."""
    if not values:
        return None
    selected: set[str] = set()
    for value in values:
        for selector in value.split(","):
            selector = selector.strip()
            if not selector:
                continue
            if "-" not in selector:
                selected.add(normalize_task_id(selector))
                continue
            pieces = [piece.strip() for piece in selector.split("-")]
            if len(pieces) != 2 or not all(pieces):
                raise ValueError(f"invalid task range: {selector!r}")
            start = int(normalize_task_id(pieces[0]))
            end = int(normalize_task_id(pieces[1]))
            if start > end:
                raise ValueError(f"task range must be ascending: {selector!r}")
            selected.update(f"{task_id:03d}" for task_id in range(start, end + 1))
    if not selected:
        raise ValueError("at least one task id is required")
    return selected


def load_rows() -> list[dict[str, object]]:
    return [json.loads(line) for line in (ROOT / "manifests" / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]


def task_source(
    task_path: str,
    *,
    root: Path = ROOT,
    include_build_context: bool = False,
) -> Path:
    source = root / task_path
    if include_build_context:
        if source.is_dir():
            return source
        raise FileNotFoundError(f"full build context is absent: {task_path}")
    snapshot_source = root / "huggingface" / task_path
    if snapshot_source.is_dir():
        return snapshot_source
    if source.is_dir():
        return source
    raise FileNotFoundError(f"task bundle is absent from local and HF snapshots: {task_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "tasks-selected")
    parser.add_argument(
        "--task-id", action="append", dest="task_ids",
        help="Task id selector; repeat or use commas/ranges, e.g. 002,005-007",
    )
    parser.add_argument(
        "--allow-restricted-licenses",
        action="store_true",
        dest="allow_restricted_licenses",
        help="Allow GPL-family and non-commercial/restricted-license tasks in the materialized selection",
    )
    parser.add_argument(
        "--include-build-context",
        action="store_true",
        help="Copy full environment source/build inputs instead of the thin HF task bundle",
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    selected = expand_task_selectors(args.task_ids)
    available_rows = load_rows()
    available_ids = {str(row["release_id"]) for row in available_rows}
    if selected is not None:
        unknown = selected - available_ids
        if unknown:
            raise ValueError(f"unknown task ids: {', '.join(sorted(unknown))}")
    matched = [
        row for row in available_rows
        if selected is None or str(row["release_id"]) in selected
    ]
    restricted_gated = [
        str(row["release_id"])
        for row in matched
        if str(row.get("license_gate", "none")) != "none"
    ]
    if selected is not None and restricted_gated and not args.allow_restricted_licenses:
        raise ValueError(
            "restricted-license task selection requires --allow-restricted-licenses: "
            + ", ".join(restricted_gated)
        )
    rows = [
        row for row in matched
        if str(row.get("license_gate", "none")) == "none"
        or args.allow_restricted_licenses
    ]
    if args.output.exists():
        if not args.force:
            raise FileExistsError(f"output exists; use --force: {args.output}")
        shutil.rmtree(args.output)
    args.output.mkdir(parents=True)
    for row in rows:
        source = task_source(
            str(row["task_path"]),
            include_build_context=args.include_build_context,
        )
        destination = args.output / source.name
        if args.include_build_context:
            if not (source / "environment" / "repo").is_dir():
                raise ValueError(
                    "full build context is absent from this snapshot; "
                    "use the thin prebuilt-image bundle"
                )
            shutil.copytree(source, destination)
            continue
        destination.mkdir(parents=True)
        for relative in (
            "task.toml",
            "instruction.md",
            "metadata.json",
            "environment/Dockerfile",
            "tests/Dockerfile",
            "tests/test.sh",
        ):
            path = source / relative
            if path.is_file():
                target = destination / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
    selection = {
        "allow_restricted_licenses": args.allow_restricted_licenses,
        "task_ids": [str(row["release_id"]) for row in rows],
    }
    (args.output / "selection.json").write_text(json.dumps(selection, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(selection, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
