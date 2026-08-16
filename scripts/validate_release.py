#!/usr/bin/env python3
"""Validate release metadata and enforce the no-answer-material boundary."""

from __future__ import annotations

import argparse
import json
import re
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
        if policy:
            task_dir = ROOT / str(row["task_path"])
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
                if next(task_dir.glob(str(pattern)), None) is not None:
                    raise ValueError(
                        f"excluded material glob remains in task {task_id}: {pattern}"
                    )
            for relative, allowed_names in dict(
                policy.get("retain_subdirectories", {})
            ).items():
                parent = task_dir / str(relative)
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
                notebook = json.loads((task_dir / str(relative)).read_text(encoding="utf-8"))
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
