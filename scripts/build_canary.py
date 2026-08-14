#!/usr/bin/env python3
"""Build and inspect one task environment/verifier image pair locally."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "tasks.jsonl"


def task_language(task_id: str) -> str:
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row["release_id"] == task_id:
            return str(row.get("language") or "unknown")
    raise ValueError(f"task {task_id} is absent from manifest")


def image_slug(value: str) -> str:
    return "".join(char if char.isalnum() else "-" for char in value).strip("-").lower()


def run(command: list[str], *, capture: bool = False) -> str:
    print("+ " + " ".join(command), flush=True)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    return (completed.stdout or "").strip()


def image_info(image: str) -> dict[str, object]:
    raw = run(["docker", "image", "inspect", image], capture=True)
    payload = json.loads(raw)[0]
    return {
        "image": image,
        "id": payload.get("Id", ""),
        "os": payload.get("Os", ""),
        "architecture": payload.get("Architecture", ""),
        "repo_digests": payload.get("RepoDigests", []),
    }


def update_task_toml(task_id: str, environment_image: str, verifier_image: str) -> None:
    path = ROOT / "tasks" / f"task_{task_id}" / "task.toml"
    text = path.read_text(encoding="utf-8")
    text = text.replace('docker_image = "science-bench-task-environment-pending:canary"', f'docker_image = "{environment_image}"', 1)
    text = text.replace('docker_image = "science-bench-task-verifier-pending:canary"', f'docker_image = "{verifier_image}"', 1)
    path.write_text(text, encoding="utf-8")
    tests_dockerfile = ROOT / "tasks" / f"task_{task_id}" / "tests" / "Dockerfile"
    dockerfile_text = tests_dockerfile.read_text(encoding="utf-8")
    dockerfile_text = dockerfile_text.replace(
        "science-bench-task-verifier-pending:canary", verifier_image, 1
    )
    tests_dockerfile.write_text(dockerfile_text, encoding="utf-8")


def build(task_id: str, *, tag: str, platform: str) -> dict[str, object]:
    stage = ROOT / "staging" / f"task_{task_id}"
    environment = ROOT / "tasks" / f"task_{task_id}" / "environment"
    language = image_slug(task_language(task_id))
    env_image = f"science-bench-task-environment-{language}-task_{task_id}:{tag}"
    verifier_image = f"science-bench-task-verifier-{language}-task_{task_id}:{tag}"
    run([
        "docker", "build", "--platform", platform, "--pull=false",
        "-t", env_image, "-f", str(environment / "Dockerfile"), str(environment),
    ])
    run([
        "docker", "build", "--platform", platform, "--pull=false",
        "--build-arg", f"BASE_IMAGE={env_image}",
        "-t", verifier_image, "-f", str(stage / "verifier" / "Dockerfile"), str(stage / "verifier"),
    ])
    env_info = image_info(env_image)
    verifier_info = image_info(verifier_image)
    for info in (env_info, verifier_info):
        if info["os"] != "linux" or info["architecture"] != "amd64":
            raise RuntimeError(f"Expected linux/amd64 image, got {info}")
    update_task_toml(task_id, env_image, verifier_image)
    rows = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines() if line.strip()]
    for row in rows:
        if row["release_id"] == task_id:
            row.update({
                "environment_image": env_image,
                "verifier_image": verifier_image,
                "environment_image_id": env_info["id"],
                "verifier_image_id": verifier_info["id"],
                "image_platform": "linux/amd64",
                "status": "local-built",
            })
    MANIFEST.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")
    return {"task_id": task_id, "environment": env_info, "verifier": verifier_info}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", required=True)
    parser.add_argument("--tag", default="canary")
    parser.add_argument("--platform", default="linux/amd64")
    args = parser.parse_args()
    print(json.dumps(build(f"{int(args.task_id):03d}", tag=args.tag, platform=args.platform), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
