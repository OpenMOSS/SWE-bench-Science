#!/usr/bin/env python3
"""Patch-publish public-material changes on top of existing Docker images."""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "tasks.jsonl"
ID_RE = re.compile(r"^(?:task_)?(\d{1,3})$")


def normalize(value: str) -> str:
    match = ID_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"invalid task id: {value!r}")
    task_id = f"{int(match.group(1)):03d}"
    if task_id == "120" or not 1 <= int(task_id) <= 119:
        raise ValueError(f"release task id must be 001..119: {value!r}")
    return task_id


def rows_from_text(text: str) -> dict[str, dict[str, object]]:
    return {
        str(row["release_id"]): row
        for row in (json.loads(line) for line in text.splitlines() if line.strip())
    }


def current_rows() -> list[dict[str, object]]:
    return [
        json.loads(line)
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def old_rows() -> dict[str, dict[str, object]]:
    text = subprocess.check_output(
        ["git", "show", "HEAD:manifests/tasks.jsonl"],
        cwd=ROOT,
        text=True,
    )
    return rows_from_text(text)


def registry_env() -> dict[str, str]:
    env = os.environ.copy()
    for name in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        env.pop(name, None)
    return env


def run(command: list[str], *, capture: bool = False) -> str:
    print("+ " + " ".join(command), flush=True)
    result = subprocess.run(
        command,
        cwd=ROOT,
        env=registry_env() if command[:2] in (["docker", "pull"], ["docker", "push"]) else os.environ.copy(),
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    return (result.stdout or "").strip()


def push(reference: str) -> str:
    for attempt in range(1, 4):
        try:
            output = run(["docker", "push", reference], capture=True)
            match = re.search(r"digest:\s*(sha256:[0-9a-f]{64})", output)
            if not match:
                raise RuntimeError(f"docker push returned no digest for {reference}: {output}")
            return match.group(1)
        except (subprocess.CalledProcessError, RuntimeError) as exc:
            if attempt == 3:
                raise
            print(f"! retrying push {attempt}/3 for {reference}: {exc}", flush=True)
    raise AssertionError("unreachable")


def pull(reference: str) -> None:
    for attempt in range(1, 6):
        try:
            run(["docker", "pull", reference])
            return
        except subprocess.CalledProcessError as exc:
            if attempt == 5:
                raise
            print(f"! retrying pull {attempt}/5 for {reference}: {exc}", flush=True)


def update_manifest(task_id: str, env_ref: str, env_digest: str, verifier_ref: str, verifier_digest: str) -> None:
    rows = current_rows()
    for row in rows:
        if str(row.get("release_id")) != task_id:
            continue
        row.update(
            {
                "environment_image": f"{env_ref}@{env_digest}",
                "environment_image_tag": env_ref,
                "environment_image_digest": env_digest,
                "environment_image_id": env_digest,
                "verifier_image": f"{verifier_ref}@{verifier_digest}",
                "verifier_image_tag": verifier_ref,
                "verifier_image_digest": verifier_digest,
                "verifier_image_id": verifier_digest,
                "image_platform": "linux/amd64",
                "status": "dockerhub-published",
            }
        )
        break
    else:
        raise ValueError(f"task {task_id} is absent from the manifest")
    MANIFEST.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in sorted(rows, key=lambda item: str(item["release_id"]))),
        encoding="utf-8",
    )


def update_bundle(task_id: str, env_image: str, verifier_image: str) -> None:
    for root in (ROOT / "tasks", ROOT / "huggingface" / "tasks"):
        task_dir = root / f"task_{task_id}"
        task_toml = task_dir / "task.toml"
        if task_toml.is_file():
            section = ""
            lines: list[str] = []
            for line in task_toml.read_text(encoding="utf-8").splitlines():
                stripped = line.strip()
                if stripped.startswith("["):
                    section = stripped
                if stripped.startswith("docker_image") and section == "[environment]":
                    line = f'docker_image = "{env_image}"'
                elif stripped.startswith("docker_image") and section == "[verifier.environment]":
                    line = f'docker_image = "{verifier_image}"'
                lines.append(line)
            task_toml.write_text("\n".join(lines) + "\n", encoding="utf-8")
        dockerfile = task_dir / "tests" / "Dockerfile"
        if dockerfile.is_file():
            text = dockerfile.read_text(encoding="utf-8")
            dockerfile.write_text(
                re.sub(r"ARG VERIFIER_IMAGE=.*", f"ARG VERIFIER_IMAGE={verifier_image}", text, count=1),
                encoding="utf-8",
            )


def build_patch(builder: str, reference: str, base: str, task_id: str, context: Path, metadata: Path) -> str:
    metadata.parent.mkdir(parents=True, exist_ok=True)
    dockerfile = context / "Dockerfile"
    dockerfile.write_text(
        "FROM " + base + "\n"
        "COPY overlay/ /app/task_" + task_id + "/\n"
        "RUN git config user.email science-bench@example.invalid && "
        "git config user.name 'SWE-bench Science baseline' && "
        "git add -A && git commit --amend --no-edit && "
        "git reflog expire --expire=now --all && git gc --prune=now\n",
        encoding="utf-8",
    )
    run(
        [
            "docker", "buildx", "build", "--builder", builder,
            "--platform", "linux/amd64", "--pull=false", "--provenance=false",
            "--sbom=false", "--load", "--tag", reference,
            "--metadata-file", str(metadata), "--file", str(dockerfile), str(context),
        ]
    )
    platform = run(["docker", "image", "inspect", "--format", "{{.Os}}/{{.Architecture}}", reference], capture=True)
    if platform != "linux/amd64":
        raise RuntimeError(f"patched image is not linux/amd64: {reference} -> {platform}")
    digest = push(reference)
    metadata.write_text(json.dumps({"containerimage.digest": digest}, indent=2) + "\n", encoding="utf-8")
    return digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", action="append", required=True)
    parser.add_argument("--registry", default="docker.io/kevinxulearning")
    parser.add_argument("--tag", default="v0.1.1")
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--builder", default="desktop-linux")
    args = parser.parse_args()
    task_ids = list(dict.fromkeys(normalize(value) for value in args.task_id))
    if args.batch_size <= 0:
        raise ValueError("--batch-size must be positive")
    current = rows_from_text(MANIFEST.read_text(encoding="utf-8"))
    previous = old_rows()
    for task_id in task_ids:
        for key in ("environment_image", "verifier_image"):
            if not str(previous.get(task_id, {}).get(key) or "").startswith("docker.io/"):
                raise ValueError(f"HEAD has no reusable {key} for task {task_id}")
        if not (ROOT / "tasks" / f"task_{task_id}" / "environment" / "public").is_dir():
            raise FileNotFoundError(f"missing public overlay for {task_id}")
    run(["docker", "buildx", "inspect", "--builder", args.builder, "--bootstrap"])
    publish_root = ROOT / "build" / "patch-publish"
    for batch_number, start in enumerate(range(0, len(task_ids), args.batch_size), start=1):
        batch_root = publish_root / f"batch-{batch_number:03d}"
        batch_root.mkdir(parents=True, exist_ok=True)
        references: list[str] = []
        try:
            for task_id in task_ids[start : start + args.batch_size]:
                old = previous[task_id]
                old_env = str(old["environment_image"])
                old_verifier = str(old["verifier_image"])
                pull(old_env)
                pull(old_verifier)
                overlay = ROOT / "tasks" / f"task_{task_id}" / "environment" / "public"
                env_context = batch_root / task_id / "environment"
                verifier_context = batch_root / task_id / "verifier"
                for context in (env_context, verifier_context):
                    (context / "overlay").mkdir(parents=True, exist_ok=True)
                    shutil.copytree(overlay, context / "overlay", dirs_exist_ok=True)
                language = re.sub(r"[^a-z0-9]+", "-", str(current[task_id].get("language") or "unknown").lower()).strip("-")
                env_ref = f"{args.registry}/swe-bench-science-environment-{language}-task-{task_id}:{args.tag}"
                verifier_ref = f"{args.registry}/swe-bench-science-verifier-{language}-task-{task_id}:{args.tag}"
                references.extend([env_ref, verifier_ref])
                env_digest = build_patch(args.builder, env_ref, old_env, task_id, env_context, batch_root / f"{task_id}-environment.json")
                verifier_digest = build_patch(args.builder, verifier_ref, old_verifier, task_id, verifier_context, batch_root / f"{task_id}-verifier.json")
                update_manifest(task_id, env_ref, env_digest, verifier_ref, verifier_digest)
                update_bundle(task_id, f"{env_ref}@{env_digest}", f"{verifier_ref}@{verifier_digest}")
                print(json.dumps({"task_id": task_id, "environment": f"{env_ref}@{env_digest}", "verifier": f"{verifier_ref}@{verifier_digest}"}, indent=2), flush=True)
        finally:
            for reference in references:
                subprocess.run(["docker", "image", "rm", "-f", reference], cwd=ROOT, check=False)
            subprocess.run(["docker", "image", "prune", "--force"], cwd=ROOT, check=False)
            subprocess.run(["docker", "buildx", "prune", "--builder", args.builder, "--force"], cwd=ROOT, check=False)
    run(["python3", "scripts/generate_huggingface.py"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
