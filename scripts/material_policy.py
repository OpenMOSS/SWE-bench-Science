#!/usr/bin/env python3
"""Apply audited auxiliary-material distribution policy to task contexts."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "manifests" / "materials.jsonl"
SUPPLEMENTAL_POLICY_PATHS = (
    ROOT / "manifests" / "materials_061_075.jsonl",
    ROOT / "manifests" / "materials_091_105.json",
)


def load_policies() -> dict[str, dict[str, object]]:
    policy_paths = [path for path in (POLICY_PATH, *SUPPLEMENTAL_POLICY_PATHS) if path.is_file()]
    if not policy_paths:
        return {}
    policies: dict[str, dict[str, object]] = {}
    for path in policy_paths:
        if path.suffix == ".jsonl":
            loaded = [
                json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip()
            ]
        else:
            loaded = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(loaded, list):
                raise ValueError(f"material policy file must contain a list: {path}")
        for policy in loaded:
            if not isinstance(policy, dict):
                raise ValueError(f"material policy entry must be an object: {path}")
            # Keep every material record schema-complete. Benchmark-authored
            # files do not carry a third-party license, so their fields are
            # deliberately empty rather than omitted.
            normalized = dict(policy)
            materials = []
            for material in policy.get("materials", []):
                if isinstance(material, dict):
                    material = dict(material)
                    if "benchmark_" in str(material.get("kind", "")).lower():
                        material.setdefault("license", "")
                        material.setdefault("copyright", "")
                materials.append(material)
            normalized["materials"] = materials
            task_id = str(normalized["task_id"])
            if task_id in policies:
                raise ValueError(f"duplicate material policy for task {task_id}")
            policies[task_id] = normalized
    return policies


def _task_path(task_dir: Path, relative: str) -> Path:
    candidate = (task_dir / relative).resolve()
    task_root = task_dir.resolve()
    if candidate != task_root and task_root not in candidate.parents:
        raise ValueError(f"material policy path escapes task root: {relative}")
    return candidate


def _root_path(relative: str) -> Path:
    candidate = (ROOT / relative).resolve()
    root = ROOT.resolve()
    if candidate != root and root not in candidate.parents:
        raise ValueError(f"material override path escapes release root: {relative}")
    return candidate


def _clear_notebook_outputs(path: Path) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    for cell in notebook.get("cells", []):
        if cell.get("cell_type") == "code":
            cell["execution_count"] = None
            cell["outputs"] = []
    metadata = notebook.get("metadata")
    if isinstance(metadata, dict):
        metadata.pop("widgets", None)
    path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )


def _material_payload(policy: dict[str, object]) -> dict[str, object]:
    return {
        "schema_version": policy["schema_version"],
        "task_id": policy["task_id"],
        "reviewed_on": policy["reviewed_on"],
        "review_standard": policy["review_standard"],
        "requires_restricted_gate": bool(policy.get("requires_restricted_gate")),
        "restricted_reason": policy.get("restricted_reason", ""),
        "materials": policy.get("materials", []),
    }


def _material_notice(payload: dict[str, object]) -> str:
    lines = [
        "# Auxiliary Material Licenses",
        "",
        f"Audit date: `{payload['reviewed_on']}`",
        "",
        str(payload["review_standard"]),
        "",
    ]
    if payload.get("requires_restricted_gate"):
        lines.extend(
            [
                "This task requires explicit restricted-license opt-in.",
                "",
                f"Reason: {payload.get('restricted_reason', '')}",
                "",
            ]
        )
    for material in payload.get("materials", []):
        if not isinstance(material, dict):
            continue
        lines.extend(
            [
                f"## `{material.get('path', '')}`",
                "",
                f"- Kind: `{material.get('kind', '')}`",
                f"- Distribution decision: `{material.get('distribution_decision', '')}`",
                f"- License: `{material.get('license', '')}`",
                f"- Source: <{material.get('source_url', '')}>",
                f"- Copyright: {material.get('copyright', '')}",
                f"- Modified or converted: `{'yes' if material.get('modified') else 'no'}`",
                f"- Third-party exceptions: {material.get('third_party_exceptions', '')}",
            ]
        )
        if material.get("notes"):
            lines.append(f"- Notes: {material['notes']}")
        lines.append("")
    return "\n".join(lines)


def materials_digest(payload: dict[str, object]) -> str:
    data = (json.dumps(payload, sort_keys=True, ensure_ascii=False) + "\n").encode()
    return hashlib.sha256(data).hexdigest()


def material_license_summary(policy: dict[str, object]) -> str:
    licenses = {
        str(material.get("license"))
        for material in policy.get("materials", [])
        if isinstance(material, dict)
        and material.get("distribution_decision") in {"bundled", "restricted"}
        and material.get("license")
    }
    return "; ".join(sorted(licenses))


def audited_source_license(policy: dict[str, object]) -> str:
    for material in policy.get("materials", []):
        if isinstance(material, dict) and str(material.get("kind", "")).endswith(
            "source_snapshot"
        ):
            return str(material.get("license", ""))
    return ""


def apply_task_policy(task_id: str, task_dir: Path) -> dict[str, object] | None:
    policy = load_policies().get(task_id)
    if policy is None:
        return None

    for relative in policy.get("remove", []):
        target = _task_path(task_dir, str(relative))
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists() or target.is_symlink():
            target.unlink()

    for pattern in policy.get("remove_globs", []):
        # Delete deepest paths first so a matched parent cannot invalidate a
        # still-pending child path. glob() remains rooted in the task bundle.
        matches = sorted(
            task_dir.glob(str(pattern)),
            key=lambda path: len(path.parts),
            reverse=True,
        )
        for target in matches:
            _task_path(task_dir, str(target.relative_to(task_dir)))
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
            elif target.exists() or target.is_symlink():
                target.unlink()

    for relative, allowed_names in dict(policy.get("retain_subdirectories", {})).items():
        parent = _task_path(task_dir, str(relative))
        if not parent.is_dir():
            raise FileNotFoundError(parent)
        allowed = {str(name) for name in allowed_names}
        for child in parent.iterdir():
            if child.is_dir() and child.name not in allowed:
                shutil.rmtree(child)

    for relative, allowed_names in dict(policy.get("retain_files", {})).items():
        parent = _task_path(task_dir, str(relative))
        if not parent.is_dir():
            raise FileNotFoundError(parent)
        allowed = {str(name) for name in allowed_names}
        for child in parent.iterdir():
            if child.is_file() and child.name not in allowed:
                child.unlink()

    for destination, source in dict(policy.get("overrides", {})).items():
        source_path = _root_path(str(source))
        if not source_path.is_file():
            raise FileNotFoundError(source_path)
        destination_path = _task_path(task_dir, str(destination))
        destination_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, destination_path)

    overlay = ROOT / "material_overrides" / f"task_{task_id}" / "task_overlay"
    if overlay.is_dir():
        shutil.copytree(overlay, task_dir, dirs_exist_ok=True)

    for relative in policy.get("strip_notebook_outputs", []):
        notebook = _task_path(task_dir, str(relative))
        if not notebook.is_file():
            raise FileNotFoundError(notebook)
        _clear_notebook_outputs(notebook)

    payload = _material_payload(policy)
    materials_path = task_dir / "environment" / "public" / "MATERIALS.json"
    materials_path.parent.mkdir(parents=True, exist_ok=True)
    materials_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (materials_path.parent / "MATERIALS_LICENSES.md").write_text(
        _material_notice(payload),
        encoding="utf-8",
    )

    auxiliary_path = materials_path.parent / "auxiliary_materials.json"
    if auxiliary_path.is_file():
        auxiliary = json.loads(auxiliary_path.read_text(encoding="utf-8"))
        entries = auxiliary.setdefault("auxiliary_materials", [])
        if not any(entry.get("path") == "MATERIALS.json" for entry in entries):
            entries.append({"path": "MATERIALS.json", "kind": "license_manifest"})
        if not any(entry.get("path") == "MATERIALS_LICENSES.md" for entry in entries):
            entries.append(
                {"path": "MATERIALS_LICENSES.md", "kind": "license_notice"}
            )
        auxiliary_path.write_text(
            json.dumps(auxiliary, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )

    return {
        "audited_source_license": audited_source_license(policy),
        "release_metadata": dict(policy.get("release_metadata", {})),
        "materials_gate": bool(policy.get("requires_restricted_gate")),
        "restricted_reason": str(policy.get("restricted_reason", "")),
        "materials_license_summary": material_license_summary(policy),
        "materials_manifest_sha256": materials_digest(payload),
    }


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", action="append", required=True)
    args = parser.parse_args()
    for task_id in args.task_id:
        normalized = f"{int(task_id.removeprefix('task_')):03d}"
        result = apply_task_policy(normalized, ROOT / "tasks" / f"task_{normalized}")
        if result is None:
            raise ValueError(f"no material policy for task {normalized}")
        print(json.dumps({"task_id": normalized, **result}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
