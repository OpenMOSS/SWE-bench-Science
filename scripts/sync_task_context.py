#!/usr/bin/env python3
"""Synchronize one release task's generated runtime and verifier context.

This command intentionally accepts one task id per invocation.  It updates
only generated files: the archived source, fixtures, and private tests are
never rewritten.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from import_task import (
    ROOT,
    render_package_source_args,
    render_runtime_environment_lines,
    render_source_build_lines,
    render_verifier_source_build_lines,
    render_system_package_lines,
    render_template,
    runtime_options,
    write_requirements_lock,
)


def normalize_task_id(value: str) -> str:
    value = value.strip().removeprefix("task_")
    if not value.isdigit() or not 1 <= int(value) <= 119:
        raise ValueError(f"task id must be in 001..119: {value!r}")
    return f"{int(value):03d}"


def manifest_language(task_id: str) -> str:
    for line in (ROOT / "manifests" / "tasks.jsonl").read_text().splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if str(row.get("release_id")) == task_id:
            return str(row.get("language") or "unknown")
    raise ValueError(f"task {task_id} is absent from manifests/tasks.jsonl")


def image_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unknown"


def existing_base_image(path: Path) -> str:
    match = re.search(r"^ARG BASE_IMAGE=([^\n]+)$", path.read_text(), re.MULTILINE)
    if not match:
        raise ValueError(f"missing BASE_IMAGE in {path}")
    return match.group(1).strip()


def merged_dependencies(lock: Path, additions: list[str]) -> list[str]:
    values = [
        line.strip()
        for line in lock.read_text().splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    for value in additions:
        if value not in values:
            values.append(value)
    return values or ["pytest==8.3.5"]


def sync(task_id: str, *, add_python: list[str], add_system: list[str]) -> None:
    task_dir = ROOT / "tasks" / f"task_{task_id}"
    environment = task_dir / "environment"
    public_task = environment / "public" / "task.json"
    dockerfile = environment / "Dockerfile"
    lock = environment / "requirements.lock"
    staging = ROOT / "staging" / f"task_{task_id}" / "verifier"
    if not public_task.is_file() or not dockerfile.is_file() or not staging.is_dir():
        raise FileNotFoundError(f"incomplete generated context for task {task_id}")

    task_data = json.loads(public_task.read_text())
    runtime = runtime_options(task_data)
    base_image = runtime["base_image"] or existing_base_image(dockerfile)
    language = manifest_language(task_id)
    system_packages = list(runtime["system_packages"])
    for value in add_system:
        if value not in system_packages:
            system_packages.append(value)

    declared = runtime["python_packages"]
    if declared is None:
        write_requirements_lock(
            environment / "repo",
            lock,
            task_id=task_id,
            language=language,
            declared_dependencies=merged_dependencies(lock, add_python),
        )
    else:
        dependencies = list(declared)
        for value in add_python:
            if value not in dependencies:
                dependencies.append(value)
        write_requirements_lock(
            environment / "repo",
            lock,
            task_id=task_id,
            language=language,
            declared_dependencies=dependencies,
        )

    render_template(
        ROOT / "templates" / "environment" / "Dockerfile",
        dockerfile,
        task_id=task_id,
        replacements={
            "ARG BASE_IMAGE=python:3.11-slim": f"ARG BASE_IMAGE={base_image}",
            "ARG INSTALL_FORTRAN=0": (
                f"ARG INSTALL_FORTRAN={int(language in {'fortran', 'c', 'c++', 'python-cython', 'python-cpp'})}"
            ),
            "ARG INSTALL_OCTAVE=0": f"ARG INSTALL_OCTAVE={int(language == 'matlab-octave')}",
            "__SYSTEM_PACKAGE_LINES__": render_system_package_lines(system_packages),
            "__PIP_EXTRA_INDEX_ARGS__": render_package_source_args(runtime["python_package_sources"]),
            "__SOURCE_BUILD_LINES__": render_source_build_lines(task_id, task_data.get("environment", {}).get("source_build") if isinstance(task_data.get("environment", {}), dict) else None),
            "__RUNTIME_ENVIRONMENT_LINES__": render_runtime_environment_lines(runtime["environment_variables"]),
        },
    )

    # The staging directory is ignored by git and is consumed only while an
    # image is built. Render the current directory-discovery grader so an old
    # hard-coded test filename cannot turn a dependency repair into a false
    # infrastructure failure.
    for name in ("Dockerfile", "test.sh", "grader.py"):
        render_template(
            ROOT / "templates" / "verifier" / name,
            staging / name,
            task_id=task_id,
            replacements={
                "__SOURCE_BUILD_CLEAN_FLAGS__": (
                    "ffd" if runtime.get("source_build") else "ffdqx"
                ),
                "__SOURCE_BUILD_RUNTIME_LINES__": render_verifier_source_build_lines(
                    task_id, runtime.get("source_build")
                )
            },
        )
    print(
        json.dumps(
            {
                "task_id": task_id,
                "base_image": base_image,
                "python_packages": [
                    line
                    for line in lock.read_text().splitlines()
                    if line.strip() and not line.startswith("#")
                ],
                "system_packages": system_packages,
                "source_build": runtime.get("source_build"),
            },
            indent=2,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--add-python", action="append", default=[])
    parser.add_argument("--add-system", action="append", default=[])
    args = parser.parse_args()
    sync(
        normalize_task_id(args.task_id),
        add_python=args.add_python,
        add_system=args.add_system,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
