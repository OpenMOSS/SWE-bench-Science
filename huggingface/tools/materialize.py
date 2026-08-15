#!/usr/bin/env python3
"""Materialize an explicit local Pier task selection from the release table."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GPL_IDS = {"003", "021", "023", "057", "066", "074", "075", "083", "084", "085", "100", "118"}


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


def task_source(task_path: str, *, root: Path = ROOT) -> Path:
    source = root / task_path
    if source.is_dir():
        return source
    snapshot_source = root / "huggingface" / task_path
    if snapshot_source.is_dir():
        return snapshot_source
    raise FileNotFoundError(f"task bundle is absent from local and HF snapshots: {task_path}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "tasks-selected")
    parser.add_argument(
        "--task-id", action="append", dest="task_ids",
        help="Task id selector; repeat or use commas/ranges, e.g. 002,005-007",
    )
    parser.add_argument(
        "--allow-GPL", "--allow-gpl", action="store_true", dest="allow_gpl",
        help="Allow the 12 GPL-family tasks in the materialized selection",
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
    gated = [str(row["release_id"]) for row in matched if bool(row.get("gpl_family"))]
    if gated and not args.allow_gpl:
        raise ValueError(
            "GPL-family task selection requires --allow-GPL: " + ", ".join(gated)
        )
    rows = [row for row in matched if args.allow_gpl or not bool(row.get("gpl_family"))]
    if args.output.exists():
        if not args.force:
            raise FileExistsError(f"output exists; use --force: {args.output}")
        shutil.rmtree(args.output)
    args.output.mkdir(parents=True)
    for row in rows:
        source = task_source(str(row["task_path"]))
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
        "allow_gpl": args.allow_gpl,
        "task_ids": [str(row["release_id"]) for row in rows],
    }
    (args.output / "selection.json").write_text(json.dumps(selection, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(selection, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
