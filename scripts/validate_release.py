#!/usr/bin/env python3
"""Validate release metadata and enforce the no-answer-material boundary."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier.
    import tomli as tomllib
from pathlib import Path

try:
    from .material_policy import (
        audited_source_license,
        load_policies,
        material_license_summary,
        materials_digest,
    )
except ImportError:  # Direct execution from the scripts directory.
    import sys

    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from scripts.material_policy import (
        audited_source_license,
        load_policies,
        material_license_summary,
        materials_digest,
    )


ROOT = Path(__file__).resolve().parents[1]
SECRET_RE = re.compile(r"(?i)(sk-[a-z0-9]{20,}|ghp_[a-z0-9]{20,}|bearer\s+[a-z0-9._-]{20,})")
FORBIDDEN_PARTS = {"solution", "oracle", "author_notes", "reference_patches"}


def load_rows() -> list[dict[str, object]]:
    path = ROOT / "manifests" / "tasks.jsonl"
    if not path.is_file():
        raise FileNotFoundError(path)
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def validate_release_provenance(rows: list[dict[str, object]]) -> None:
    """Keep the published provenance record aligned with both manifests."""
    manifest_path = ROOT / "manifests" / "tasks.jsonl"
    provenance_path = ROOT / "manifests" / "release_provenance.json"
    if not provenance_path.is_file():
        raise ValueError(f"missing release provenance: {provenance_path}")
    try:
        provenance = json.loads(provenance_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid release provenance: {provenance_path}") from exc
    image_provenance = provenance.get("image_provenance", {})
    manifest_sha256 = hashlib.sha256(manifest_path.read_bytes()).hexdigest()
    if image_provenance.get("manifest_sha256") != manifest_sha256:
        raise ValueError("release provenance manifest_sha256 is stale")
    if image_provenance.get("task_count") != len(rows):
        raise ValueError("release provenance task_count mismatch")
    if image_provenance.get("environment_digest_count") != sum(
        bool(row.get("environment_image_digest")) for row in rows
    ):
        raise ValueError("release provenance environment digest count mismatch")
    if image_provenance.get("verifier_digest_count") != sum(
        bool(row.get("verifier_image_digest")) for row in rows
    ):
        raise ValueError("release provenance verifier digest count mismatch")
    if image_provenance.get("platform") != "linux/amd64":
        raise ValueError("release provenance platform must be linux/amd64")
    mirror_path = ROOT / "huggingface" / "manifests" / "tasks.jsonl"
    if mirror_path.is_file() and mirror_path.read_bytes() != manifest_path.read_bytes():
        raise ValueError("Hugging Face manifest is not byte-identical to canonical manifest")
    mirror_provenance = ROOT / "huggingface" / "manifests" / provenance_path.name
    if mirror_provenance.is_file() and mirror_provenance.read_bytes() != provenance_path.read_bytes():
        raise ValueError("Hugging Face release provenance is not byte-identical")


def scan_files() -> list[str]:
    findings: list[str] = []
    roots = [ROOT / "tasks", ROOT / "staging", ROOT / "huggingface", ROOT / "manifests"]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            relative = path.relative_to(ROOT)
            if any(part in FORBIDDEN_PARTS for part in relative.parts):
                findings.append(f"forbidden path: {relative}")
                continue
            if "private_tests" in relative.parts and not (
                len(relative.parts) >= 4
                and relative.parts[0] == "staging"
                and relative.parts[2] in {"verifier", "verifier_release"}
            ):
                findings.append(f"private tests outside verifier staging: {relative}")
                continue
            if path.name.lower() in {"solution.patch", "gold.patch", "reference.patch", "model.patch"}:
                findings.append(f"forbidden answer artifact: {relative}")
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if SECRET_RE.search(text):
                findings.append(f"secret-like value: {relative}")
    return findings


def is_gpl_family_license(value: object) -> bool:
    return "GPL" in str(value).upper()


def is_restricted_license(row: dict[str, object]) -> bool:
    return (
        is_gpl_family_license(row.get("source_license"))
        or str(row.get("source_license", "")) == "Academic-NonCommercial"
        or bool(row.get("material_restricted"))
    )


def validate_task_image_references(
    row: dict[str, object], thin_task_path: Path
) -> None:
    """Require task-local image refs to equal the canonical manifest pair."""
    environment_image = str(row.get("environment_image") or "")
    verifier_image = str(row.get("verifier_image") or "")
    if not environment_image and not verifier_image:
        return
    task_toml = thin_task_path / "task.toml"
    if not task_toml.is_file():
        raise ValueError(f"missing task.toml for {row['release_id']}")
    try:
        payload = tomllib.loads(task_toml.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError as exc:
        raise ValueError(f"invalid task.toml for {row['release_id']}: {exc}") from exc
    task_environment = str(
        payload.get("environment", {}).get("docker_image", "")
    )
    task_verifier = str(
        payload.get("verifier", {}).get("environment", {}).get("docker_image", "")
    )
    if task_environment != environment_image:
        raise ValueError(
            f"environment image mismatch for {row['release_id']}: "
            f"task.toml={task_environment!r}, manifest={environment_image!r}"
        )
    if task_verifier != verifier_image:
        raise ValueError(
            f"verifier image mismatch for {row['release_id']}: "
            f"task.toml={task_verifier!r}, manifest={verifier_image!r}"
        )
    dockerfile = thin_task_path / "tests" / "Dockerfile"
    if dockerfile.is_file():
        match = re.search(r"^ARG VERIFIER_IMAGE=(\S+)$", dockerfile.read_text(encoding="utf-8"), re.MULTILINE)
        if not match:
            raise ValueError(f"missing VERIFIER_IMAGE in {dockerfile}")
        if match.group(1) != verifier_image:
            raise ValueError(
                f"verifier Dockerfile mismatch for {row['release_id']}: "
                f"Dockerfile={match.group(1)!r}, manifest={verifier_image!r}"
            )


def expected_license_gate(row: dict[str, object]) -> str:
    if is_gpl_family_license(row.get("source_license")):
        return "gpl-family"
    if str(row.get("source_license", "")) == "Academic-NonCommercial":
        return "noncommercial"
    if bool(row.get("material_restricted")):
        normalized_material_license = str(row.get("material_license", "")).upper().replace("-", "")
        return (
            "noncommercial"
            if "NONCOMMERCIAL" in normalized_material_license
            else "restricted-materials"
        )
    return "none"


def validate(*, require_images: bool) -> dict[str, object]:
    rows = load_rows()
    validate_release_provenance(rows)
    material_policies = load_policies()
    ids = [str(row.get("release_id", "")) for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate release_id")
    for task_id in ids:
        if not re.fullmatch(r"\d{3}", task_id):
            raise ValueError(f"invalid release_id: {task_id!r}")
        if task_id == "120":
            raise ValueError("legacy task id 120 is forbidden")
    for row in rows:
        task_id = str(row["release_id"])
        policy = material_policies.get(task_id)
        if policy:
            expected_material_gate = bool(policy.get("requires_restricted_gate"))
            if bool(row.get("materials_gate")) != expected_material_gate:
                raise ValueError(f"materials_gate mismatch for {task_id}")
            if bool(row.get("material_restricted")) != expected_material_gate:
                raise ValueError(f"material_restricted mismatch for {task_id}")
            if str(row.get("material_license", "")) != material_license_summary(policy):
                raise ValueError(f"material license summary mismatch for {task_id}")
            if str(row.get("source_license", "")) != audited_source_license(policy):
                raise ValueError(f"audited source license mismatch for {task_id}")
            if str(row.get("restricted_reason", "")) != str(policy.get("restricted_reason", "")):
                raise ValueError(f"restricted reason mismatch for {task_id}")
        if bool(row.get("gpl_family")) != is_gpl_family_license(row.get("source_license")):
            raise ValueError(f"GPL classification mismatch for {task_id}")
        if bool(row.get("restricted_license")) != is_restricted_license(row):
            raise ValueError(f"restricted-license classification mismatch for {task_id}")
        if str(row.get("license_gate", "none")) != expected_license_gate(row):
            raise ValueError(f"license_gate mismatch for {task_id}")
        task_path = ROOT / str(row["task_path"])
        thin_task_path = ROOT / "huggingface" / "tasks" / task_path.name
        if not task_path.is_dir() and not thin_task_path.is_dir():
            raise ValueError(f"missing task bundle for {task_id}")
        for relative in (
            "tests/grader.py",
            "tests/docker-compose.yaml",
        ):
            if not (thin_task_path / relative).is_file():
                raise ValueError(f"missing dynamic verifier entrypoint for {task_id}: {relative}")
        validate_task_image_references(row, thin_task_path)
        if policy:
            task_dir = ROOT / str(row["task_path"])
            if not task_dir.is_dir():
                # The public-control repository may carry only the thin HF
                # snapshot.  Validate its retained public material files in
                # that layout instead of assuming the private authoring tree
                # is present locally.
                task_dir = thin_task_path
            materials_path = task_dir / "environment" / "public" / "MATERIALS.json"
            if not materials_path.is_file():
                raise ValueError(f"missing material manifest for {task_id}")
            materials_payload = json.loads(materials_path.read_text(encoding="utf-8"))
            if str(row.get("materials_manifest_sha256", "")) != materials_digest(materials_payload):
                raise ValueError(f"material manifest digest mismatch for {task_id}")
            for relative in policy.get("remove", []):
                if (task_dir / str(relative)).exists():
                    raise ValueError(f"excluded material remains in task {task_id}: {relative}")
            for pattern in policy.get("remove_globs", []):
                if task_dir.exists() and next(task_dir.glob(str(pattern)), None) is not None:
                    raise ValueError(
                        f"excluded material glob remains in task {task_id}: {pattern}"
                    )
            for relative, allowed_names in dict(
                policy.get("retain_subdirectories", {})
            ).items():
                parent = task_dir / str(relative)
                if not parent.is_dir():
                    continue
                allowed = {str(name) for name in allowed_names}
                unexpected = sorted(
                    child.name
                    for child in parent.iterdir()
                    if child.is_dir() and child.name not in allowed
                )
                if unexpected:
                    raise ValueError(
                        f"unexpected subdirectories remain in task {task_id} at "
                        f"{relative}: {unexpected}"
                    )
            for relative, allowed_names in dict(policy.get("retain_files", {})).items():
                parent = task_dir / str(relative)
                if not parent.is_dir():
                    continue
                allowed = {str(name) for name in allowed_names}
                unexpected = sorted(
                    child.name
                    for child in parent.iterdir()
                    if child.is_file() and child.name not in allowed
                )
                if unexpected:
                    raise ValueError(
                        f"unexpected files remain in task {task_id} at "
                        f"{relative}: {unexpected}"
                    )
            for relative in policy.get("strip_notebook_outputs", []):
                notebook_path = task_dir / str(relative)
                if not notebook_path.is_file():
                    continue
                notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
                if any(cell.get("outputs") for cell in notebook.get("cells", [])):
                    raise ValueError(f"notebook outputs remain in task {task_id}: {relative}")
        if require_images and (not row.get("environment_image") or not row.get("verifier_image")):
            raise ValueError(f"missing image reference for {task_id}")
    findings = scan_files()
    if findings:
        raise ValueError("\n".join(findings))
    return {
        "rows": len(rows),
        "gpl_family": sum(bool(row.get("gpl_family")) for row in rows),
        "restricted_license": sum(bool(row.get("restricted_license")) for row in rows),
        "unrestricted": sum(not bool(row.get("restricted_license")) for row in rows),
        "require_images": require_images,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--require-images", action="store_true")
    args = parser.parse_args()
    print(json.dumps(validate(require_images=args.require_images), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
