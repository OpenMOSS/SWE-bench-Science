#!/usr/bin/env python3
"""Import one authoring task into clean release and verifier contexts."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASKS_ROOT = ROOT / "tasks"
STAGING_ROOT = ROOT / "staging"
TEMPLATES_ROOT = ROOT / "templates"
MANIFEST_PATH = ROOT / "manifests" / "tasks.jsonl"
GPL_IDS = {
    "003", "021", "023", "057", "066", "074", "075", "083", "084", "085", "100", "118"
}
GENERATED_NAMES = {".git", "__pycache__", ".pytest_cache", "outputs", "build", "dist"}
FORBIDDEN_NAMES = {"solution", "oracle", "reference_patches", "author_notes", "provenance.json"}


def normalize_task_id(value: str) -> str:
    value = value.strip().removeprefix("task_")
    if not value.isdigit():
        raise ValueError(f"task id must be numeric or task_NNN: {value!r}")
    task_id = f"{int(value):03d}"
    if task_id == "120":
        raise ValueError("legacy release id 120 is forbidden")
    return task_id


def copy_tree(source: Path, destination: Path) -> None:
    def ignore(_directory: str, names: list[str]) -> set[str]:
        return {
            name
            for name in names
            if name in GENERATED_NAMES
            or name in FORBIDDEN_NAMES
            or name.endswith((".pyc", ".pyo", ".so", ".o", ".a"))
        }

    shutil.copytree(
        source,
        destination,
        ignore=ignore,
        symlinks=True,
        dirs_exist_ok=True,
    )


def tree_sha256(root: Path) -> str:
    digest = hashlib.sha256()
    files = (path for path in root.rglob("*") if path.is_file())
    for path in sorted(files, key=lambda item: item.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix().encode()
        data = path.read_bytes()
        digest.update(len(relative).to_bytes(8, "big"))
        digest.update(relative)
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def detect_license(source: Path) -> tuple[str, str]:
    candidates = sorted(
        (
            path
            for path in source.rglob("*")
            if path.is_file() and path.name.upper().startswith(("LICENSE", "COPYING"))
        ),
        key=lambda path: (len(path.relative_to(source).parts), path.as_posix()),
    )
    if not candidates:
        return "UNKNOWN", "not-detected"
    normalized = re.sub(
        r"\s+",
        " ",
        "\n".join(
            path.read_text(encoding="utf-8", errors="replace") for path in candidates
        ).upper(),
    )
    if "GNU AFFERO GENERAL PUBLIC LICENSE" in normalized:
        return "AGPL-family", candidates[0].name
    if "GNU LESSER GENERAL PUBLIC LICENSE" in normalized:
        if "VERSION 3" in normalized:
            return "LGPL-3.0-family", candidates[0].name
        if "VERSION 2.1" in normalized:
            return "LGPL-2.1-family", candidates[0].name
        return "LGPL-family", candidates[0].name
    if "GNU GENERAL PUBLIC LICENSE" in normalized:
        if "VERSION 3" in normalized:
            return "GPL-3.0-family", candidates[0].name
        if "VERSION 2" in normalized:
            return "GPL-2.0-family", candidates[0].name
        return "GPL-family", candidates[0].name
    if (
        "REDISTRIBUTION AND USE IN SOURCE AND BINARY FORMS" in normalized
        and "NEITHER THE NAME" in normalized
    ):
        return "BSD-3-Clause", candidates[0].name
    if (
        "MIT LICENSE" in normalized
        or "PERMISSION IS HEREBY GRANTED, FREE OF CHARGE" in normalized
    ):
        return "MIT", candidates[0].name
    if "BSD 3-CLAUSE" in normalized or "BSD-3-CLAUSE" in normalized:
        return "BSD-3-Clause", candidates[0].name
    if "BSD 2-CLAUSE" in normalized or "BSD-2-CLAUSE" in normalized:
        return "BSD-2-Clause", candidates[0].name
    if "APACHE LICENSE" in normalized and "VERSION 2.0" in normalized:
        return "Apache-2.0", candidates[0].name
    return "UNKNOWN", candidates[0].name


def render_template(
    source: Path,
    destination: Path,
    *,
    task_id: str,
    replacements: dict[str, str] | None = None,
) -> None:
    text = source.read_text(encoding="utf-8").replace("__TASK_ID__", task_id)
    for key, value in (replacements or {}).items():
        text = text.replace(key, value)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8")
    if source.stat().st_mode & 0o111:
        destination.chmod(0o755)


def base_image_for(_language: str) -> str:
    """Return the common amd64-capable base used for all language families.

    Python is the benchmark orchestration layer even for native projects. The
    image also installs C/C++/Fortran build tools, so source extensions can be
    rebuilt inside the task environment instead of relying on host binaries.
    """
    return "python:3.11-slim"


def install_octave_for(language: str) -> bool:
    return language == "matlab-octave"


def install_fortran_for(language: str) -> bool:
    return language in {"fortran", "c", "c++", "python-cython", "python-cpp"}


def dependency_lines(source: Path, *, task_id: str, language: str) -> list[str]:
    """Extract public runtime dependencies for the task-specific lock file."""
    if task_id == "002":
        return [
            "numpy==1.26.4",
            "scipy==1.13.1",
            "pyscf==2.7.0",
            "pytest==8.3.5",
        ]

    lines: list[str] = []
    requirements = source / "requirements.txt"
    if requirements.is_file():
        for raw in requirements.read_text(encoding="utf-8", errors="replace").splitlines():
            value = raw.strip()
            if value and not value.startswith("#") and not value.startswith(("-e ", "--")):
                lines.append(value)

    # A dependency list in pyproject is simple enough to parse without adding
    # a host-side TOML dependency; full build metadata stays inside the image.
    pyproject = source / "pyproject.toml"
    if not lines and pyproject.is_file():
        in_dependencies = False
        for raw in pyproject.read_text(encoding="utf-8", errors="replace").splitlines():
            value = raw.strip()
            if value.startswith("dependencies = ["):
                in_dependencies = True
                continue
            if in_dependencies and value.startswith("]"):
                break
            if in_dependencies:
                match = re.match(r"[\\\"']([^\\\"']+)[\\\"']", value.rstrip(","))
                if match:
                    lines.append(match.group(1))

    # The verifier entrypoint is pytest-based for every language family,
    # including native and Octave tasks, so keep the runner dependency explicit.
    lines.append("pytest==8.3.5")
    return list(dict.fromkeys(lines)) or ["# No Python package dependencies declared."]


def write_requirements_lock(
    source: Path,
    destination: Path,
    *,
    task_id: str,
    language: str,
) -> None:
    destination.write_text(
        "# Generated from the public task dependency declaration.\n"
        + "\n".join(dependency_lines(source, task_id=task_id, language=language))
        + "\n",
        encoding="utf-8",
    )


def task_toml(*, task_id: str, title: str, language: str, base_commit: str) -> str:
    return (
        'schema_version = "1.3"\n'
        'artifacts = ["/logs/artifacts/model.patch"]\n\n'
        '[task]\n'
        f'name = "openmoss/swe-bench-science-{task_id}"\n'
        f'description = {json.dumps(title)}\n'
        'authors = []\n'
        'keywords = ["scientific-computing", "software-engineering"]\n\n'
        '[metadata]\n'
        f'task_id = "{task_id}"\n'
        f'language = {json.dumps(language)}\n'
        f'base_commit_hash = {json.dumps(base_commit)}\n\n'
        '[agent]\nnetwork_mode = "no-network"\ntimeout_sec = 5400.0\n\n'
        '[environment]\n'
        'docker_image = "science-bench-task-environment-pending:canary"\n'
        'os = "linux"\nallow_internet = false\ncpus = 2\nmemory_mb = 8192\nstorage_mb = 20480\n'
        f'workdir = "/app/task_{task_id}"\n\n'
        '[verifier]\nnetwork_mode = "no-network"\n'
        'environment_mode = "separate"\ntimeout_sec = 1800.0\n\n'
        '[verifier.environment]\n'
        'docker_image = "science-bench-task-verifier-pending:canary"\n'
        'os = "linux"\nallow_internet = false\ncpus = 2\nmemory_mb = 8192\nstorage_mb = 20480\n'
        f'workdir = "/app/task_{task_id}"\n\n'
        '[[verifier.collect]]\n'
        f'command = "cd /app/task_{task_id} && git config --global --add safe.directory '
        f'/app/task_{task_id} && baseline=$(git rev-list --max-parents=0 --reverse HEAD | '
        'head -n 1) && git add -A && git diff --cached --binary \\"$baseline\\" > '
        '/logs/artifacts/model.patch"\n'
        'timeout_sec = 300.0\n'
    )


def load_manifest_rows() -> list[dict[str, object]]:
    if not MANIFEST_PATH.exists():
        return []
    return [
        json.loads(line)
        for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def write_manifest_row(row: dict[str, object]) -> None:
    rows = [item for item in load_manifest_rows() if item.get("release_id") != row["release_id"]]
    rows.append(row)
    rows.sort(key=lambda item: str(item["release_id"]))
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        "".join(json.dumps(item, sort_keys=True) + "\n" for item in rows),
        encoding="utf-8",
    )


def import_task(source_root: Path, task_id: str, *, force: bool) -> dict[str, object]:
    source_name = f"task_{task_id}"
    public_source = source_root / "app" / "tasks" / source_name
    private_source = source_root / "app" / "private_tests" / source_name
    if not public_source.is_dir():
        raise FileNotFoundError(public_source)
    if not private_source.is_dir():
        raise FileNotFoundError(private_source)

    task_data = json.loads((public_source / "task.json").read_text(encoding="utf-8"))
    metadata = json.loads((public_source / "metadata.json").read_text(encoding="utf-8"))
    title = str(metadata.get("title") or task_data.get("display_title") or source_name)
    language = str(metadata.get("language") or task_data.get("language") or "unknown")
    base_commit = str(metadata.get("source_commit") or "")
    source_license, license_source = detect_license(public_source / "source")

    task_dir = TASKS_ROOT / source_name
    environment_dir = task_dir / "environment"
    verifier_dir = STAGING_ROOT / source_name / "verifier"
    if force:
        shutil.rmtree(task_dir, ignore_errors=True)
        shutil.rmtree(STAGING_ROOT / source_name, ignore_errors=True)
    if task_dir.exists() or verifier_dir.exists():
        raise FileExistsError(f"task already imported; use --force: {task_dir}")

    (environment_dir / "repo").mkdir(parents=True)
    (environment_dir / "public").mkdir(parents=True)
    (verifier_dir / "private_tests").mkdir(parents=True)
    copy_tree(public_source / "source", environment_dir / "repo")
    for source in sorted(public_source.iterdir(), key=lambda item: item.name):
        if source.name in {"source", "instruction.md"}:
            continue
        destination = environment_dir / "public" / source.name
        if source.is_dir():
            copy_tree(source, destination)
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    copy_tree(private_source, verifier_dir / "private_tests")

    render_template(
        TEMPLATES_ROOT / "environment" / "Dockerfile",
        environment_dir / "Dockerfile",
        task_id=task_id,
        replacements={
            "ARG BASE_IMAGE=python:3.11-slim": f"ARG BASE_IMAGE={base_image_for(language)}",
            "ARG INSTALL_FORTRAN=0": f"ARG INSTALL_FORTRAN={int(install_fortran_for(language))}",
            "ARG INSTALL_OCTAVE=0": f"ARG INSTALL_OCTAVE={int(install_octave_for(language))}",
        },
    )
    write_requirements_lock(
        public_source / "source",
        environment_dir / "requirements.lock",
        task_id=task_id,
        language=language,
    )
    for name in ("Dockerfile", "test.sh", "grader.py"):
        render_template(
            TEMPLATES_ROOT / "verifier" / name,
            verifier_dir / name,
            task_id=task_id,
        )
    for name in ("Dockerfile", "test.sh"):
        render_template(
            TEMPLATES_ROOT / "task-tests" / name,
            task_dir / "tests" / name,
            task_id=task_id,
        )

    shutil.copy2(public_source / "instruction.md", task_dir / "instruction.md")
    (task_dir / "task.toml").write_text(
        task_toml(
            task_id=task_id,
            title=title,
            language=language,
            base_commit=base_commit,
        ),
        encoding="utf-8",
    )
    public_hash = tree_sha256(environment_dir / "public")
    release_metadata = {
        "task_id": task_id,
        "title": title,
        "domain": metadata.get("domain", "unknown"),
        "language": language,
        "source_repository": metadata.get("source_repository", ""),
        "source_commit": base_commit,
        "source_license": source_license,
        "license_source": license_source,
        "gpl_family": task_id in GPL_IDS,
        "public_payload_sha256": public_hash,
    }
    (task_dir / "metadata.json").write_text(
        json.dumps(release_metadata, indent=2) + "\n",
        encoding="utf-8",
    )
    row = {
        "schema_version": 1,
        "release_id": task_id,
        "title": title,
        "domain": metadata.get("domain", "unknown"),
        "language": language,
        "repository_url": metadata.get("source_repository", ""),
        "base_commit": base_commit,
        "source_license": source_license,
        "license_source": license_source,
        "gpl_family": task_id in GPL_IDS,
        "task_path": f"tasks/{source_name}",
        "environment_image": "",
        "verifier_image": "",
        "image_platform": "linux/amd64",
        "public_payload_sha256": public_hash,
        "status": "imported",
    }
    write_manifest_row(row)
    return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    row = import_task(
        args.source_root.resolve(),
        normalize_task_id(args.task_id),
        force=args.force,
    )
    print(json.dumps(row, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
