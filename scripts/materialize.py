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


def load_rows() -> list[dict[str, object]]:
    return [json.loads(line) for line in (ROOT / "manifests" / "tasks.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "tasks-selected")
    parser.add_argument("--task-id", action="append", dest="task_ids")
    parser.add_argument("--allow-GPL", action="store_true", dest="allow_gpl")
    parser.add_argument(
        "--include-build-context",
        action="store_true",
        help="Copy full environment source/build inputs instead of the thin HF task bundle",
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    selected = {normalize_task_id(value) for value in args.task_ids} if args.task_ids else None
    rows = []
    for row in load_rows():
        task_id = str(row["release_id"])
        if selected is not None and task_id not in selected:
            continue
        if bool(row.get("gpl_family")) and not args.allow_gpl:
            continue
        rows.append(row)
    if args.output.exists():
        if not args.force:
            raise FileExistsError(f"output exists; use --force: {args.output}")
        shutil.rmtree(args.output)
    args.output.mkdir(parents=True)
    for row in rows:
        source = ROOT / str(row["task_path"])
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
