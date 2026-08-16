#!/usr/bin/env python3
"""Build, push, record, and clean a bounded batch of task image pairs."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import tempfile
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "manifests" / "tasks.jsonl"
TASK_ID_RE = re.compile(r"^(?:task_)?(\d{1,3})$")


def normalize_task_id(value: str) -> str:
    match = TASK_ID_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"invalid task id: {value!r}")
    task_id = f"{int(match.group(1)):03d}"
    if task_id == "120" or not 1 <= int(task_id) <= 119:
        raise ValueError(f"release task id must be 001..119, got {value!r}")
    return task_id


def load_rows() -> list[dict[str, object]]:
    return [
        json.loads(line)
        for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def image_slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "unknown"


def run(command: list[str], *, capture: bool = False) -> str:
    print("+ " + " ".join(command), flush=True)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=host_network_env(),
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    return (completed.stdout or "").strip()


def host_network_env() -> dict[str, str]:
    """Translate Docker's host alias for commands executed on macOS itself."""
    env = os.environ.copy()
    for name in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        value = env.get(name)
        if value:
            env[name] = value.replace("host.docker.internal", "127.0.0.1")
    return env


def registry_network_env() -> dict[str, str]:
    """Use the direct campus route for Docker Hub registry operations."""
    env = host_network_env()
    for name in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        env.pop(name, None)
    return env


def ensure_builder(name: str) -> None:
    probe = subprocess.run(
        ["docker", "buildx", "inspect", name],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if probe.returncode != 0:
        raise RuntimeError(
            f"Docker builder {name!r} is unavailable; start Docker Desktop or choose an existing builder"
        )
    run(["docker", "buildx", "inspect", "--builder", name, "--bootstrap"])


def digest_from_metadata(path: Path) -> str:
    payload = json.loads(path.read_text(encoding="utf-8"))
    digest = str(payload.get("containerimage.digest") or "")
    if not re.fullmatch(r"sha256:[0-9a-f]{64}", digest):
        raise RuntimeError(f"buildx did not return an image digest in {path}: {payload}")
    return digest


def inspect_platform(reference: str, digest: str) -> None:
    local_platform = run(
        [
            "docker",
            "image",
            "inspect",
            "--format",
            "{{.Os}}/{{.Architecture}}",
            reference,
        ],
        capture=True,
    ).strip()
    if local_platform != "linux/amd64":
        raise RuntimeError(f"built image is not linux/amd64: {reference} -> {local_platform}")

    # Docker Desktop's current CLI can return non-zero for a valid single
    # platform OCI manifest (and `docker manifest inspect` has the same
    # limitation). Keep this probe diagnostic rather than turning a completed
    # push into a failed batch: the push digest plus the local architecture
    # check above are the release invariants.
    try:
        probe = subprocess.run(
            ["docker", "buildx", "imagetools", "inspect", f"{reference}@{digest}"],
            cwd=ROOT,
            env=registry_network_env(),
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=20,
        )
    except subprocess.TimeoutExpired as exc:
        print(f"! remote inspect timed out for {reference}@{digest}: {exc}", flush=True)
        return
    if probe.returncode != 0:
        print(f"! remote inspect unavailable for {reference}@{digest}: {probe.stdout.strip()}", flush=True)
    elif digest not in probe.stdout:
        print(f"! remote inspect did not echo digest for {reference}@{digest}", flush=True)


def build_push(
    *,
    builder: str,
    reference: str,
    dockerfile: Path,
    context: Path,
    build_args: list[str] = (),
    metadata_path: Path,
) -> str:
    metadata_path.parent.mkdir(parents=True, exist_ok=True)
    command = [
        "docker",
        "buildx",
        "build",
        "--builder",
        builder,
        "--platform",
        "linux/amd64",
        "--pull=false",
        "--provenance=false",
        "--sbom=false",
        "--load",
        "--tag",
        reference,
        "--metadata-file",
        str(metadata_path),
    ]
    for value in build_args:
        command.extend(["--build-arg", value])
    # BuildKit recognizes these proxy build args without Dockerfile changes.
    # Pass through only explicitly configured values so normal/offline builds
    # keep their existing behavior and credentials are never invented here.
    for name in ("HTTP_PROXY", "HTTPS_PROXY", "NO_PROXY", "http_proxy", "https_proxy", "no_proxy"):
        value = os.environ.get(name)
        if value:
            command.extend(["--build-arg", f"{name}={value}"])
    command.extend(["--file", str(dockerfile), str(context)])
    run(command)
    local_platform = run(
        [
            "docker",
            "image",
            "inspect",
            "--format",
            "{{.Os}}/{{.Architecture}}",
            reference,
        ],
        capture=True,
    ).strip()
    if local_platform != "linux/amd64":
        raise RuntimeError(f"built image is not linux/amd64: {reference} -> {local_platform}")
    push_output = push_with_retry(reference)
    match = re.search(r"digest:\s*(sha256:[0-9a-f]{64})", push_output)
    if not match:
        raise RuntimeError(f"docker push did not return a digest for {reference}: {push_output}")
    digest = match.group(1)
    metadata_path.write_text(
        json.dumps({"containerimage.digest": digest, "push_output": push_output}, indent=2) + "\n",
        encoding="utf-8",
    )
    inspect_platform(reference, digest)
    return digest


def push_with_retry(reference: str, *, attempts: int = 3, timeout_seconds: int = 600) -> str:
    """Retry transient registry failures without rebuilding the local image."""
    for attempt in range(1, attempts + 1):
        try:
            print("+ direct Docker Hub route", flush=True)
            completed = subprocess.run(
                ["docker", "image", "push", reference],
                cwd=ROOT,
                env=registry_network_env(),
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=timeout_seconds,
            )
            return (completed.stdout or "").strip()
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            output = (getattr(exc, "stdout", "") or "").strip()
            if isinstance(exc, subprocess.TimeoutExpired):
                output = f"push timed out after {timeout_seconds}s; {output}"
            print(
                f"! docker push attempt {attempt}/{attempts} failed for {reference}: {output[-800:]}",
                flush=True,
            )
            if attempt == attempts:
                raise
            time.sleep(5 * attempt)
    raise AssertionError("unreachable")


def smoke_verifier(reference: str, task_id: str, *, timeout_seconds: int = 2400) -> None:
    with tempfile.TemporaryDirectory(prefix=f"science-bench-smoke-{task_id}-") as directory:
        command = [
            "docker",
            "run",
            "--rm",
            "--platform",
            "linux/amd64",
            "--network",
            "none",
            "--volume",
            f"{directory}:/logs",
            reference,
        ]
        print("+ " + " ".join(command), flush=True)
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=host_network_env(),
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=timeout_seconds,
        )
        lines = [line for line in (completed.stdout or "").splitlines() if line.strip()]
        if not lines:
            raise RuntimeError(f"verifier smoke produced no output for task {task_id}")
        try:
            summary = json.loads(lines[-1])
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"verifier smoke did not end with JSON for task {task_id}: {lines[-1]}"
            ) from exc
        public_result = summary.get("public", {})
        private_result = summary.get("private", {})
        public_passed = int(public_result.get("passed", 0))
        public_collected = int(public_result.get("collected", 0))
        public_return_code = int(public_result.get("return_code", 2))
        private_collected = int(private_result.get("collected", 0))
        # A task baseline may intentionally return 1 before the agent repairs it.
        # Return code 2 is reserved by the public runners for infrastructure or
        # fixture failures and must never be accepted as a publishable smoke run.
        if public_collected < 1 or public_return_code not in {0, 1} or private_collected < 1:
            log_path = Path(directory) / "verifier" / "test-stdout.txt"
            log_tail = (
                log_path.read_text(encoding="utf-8", errors="replace")[-4000:]
                if log_path.is_file()
                else "verifier log was not written"
            )
            raise RuntimeError(
                f"verifier smoke failed for task {task_id}: "
                f"public_passed={public_passed}, public_collected={public_collected}, "
                f"public_return_code={public_return_code}, private_collected={private_collected}\n"
                f"{log_tail}"
            )
    print(
        json.dumps(
            {
                "task_id": task_id,
                "smoke_public_passed": public_passed,
                "smoke_public_return_code": public_return_code,
                "smoke_private_collected": private_collected,
                "baseline_reward": summary.get("reward"),
            },
            sort_keys=True,
        ),
        flush=True,
    )


def update_manifest(task_id: str, *, env_ref: str, env_digest: str, verifier_ref: str, verifier_digest: str) -> None:
    rows = load_rows()
    for row in rows:
        if str(row.get("release_id")) != task_id:
            continue
        row.update(
            {
                "environment_image": f"{env_ref}@{env_digest}",
                "verifier_image": f"{verifier_ref}@{verifier_digest}",
                "environment_image_tag": env_ref,
                "verifier_image_tag": verifier_ref,
                "environment_image_digest": env_digest,
                "verifier_image_digest": verifier_digest,
                # Keep the legacy image_id columns meaningful for consumers
                # that still read them: in a registry release the immutable
                # digest, rather than a local Docker daemon ID, is canonical.
                "environment_image_id": env_digest,
                "verifier_image_id": verifier_digest,
                "image_platform": "linux/amd64",
                "status": "dockerhub-published",
            }
        )
        break
    else:
        raise ValueError(f"task {task_id} is absent from manifest")
    MANIFEST_PATH.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def update_task_bundle(task_id: str, env_image: str, verifier_image: str) -> None:
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
        tests_dockerfile = task_dir / "tests" / "Dockerfile"
        if tests_dockerfile.is_file():
            text = tests_dockerfile.read_text(encoding="utf-8")
            text = re.sub(r'ARG VERIFIER_IMAGE=.*', f"ARG VERIFIER_IMAGE={verifier_image}", text, count=1)
            tests_dockerfile.write_text(text, encoding="utf-8")


def cleanup_batch(builder: str, references: list[str]) -> None:
    for reference in references:
        subprocess.run(["docker", "image", "rm", "-f", reference], cwd=ROOT, check=False)
    subprocess.run(["docker", "image", "prune", "--force"], cwd=ROOT, check=False)
    # Build cache is not a published artifact. Prune it after every bounded
    # batch so the next batch starts with the same disk budget.
    subprocess.run(["docker", "buildx", "prune", "--builder", builder, "--force"], cwd=ROOT, check=False)


def default_selection_path() -> Path:
    matches = sorted((ROOT / "huggingface" / "selections").glob("default-*.json"))
    if len(matches) != 1:
        raise FileNotFoundError("expected exactly one huggingface/selections/default-*.json")
    return matches[0]


def selected_ids(args: argparse.Namespace, rows: dict[str, dict[str, object]]) -> list[str]:
    if args.task_id:
        values = [normalize_task_id(value) for value in args.task_id]
    else:
        selection_path = ROOT / args.selection if args.selection else default_selection_path()
        payload = json.loads(selection_path.read_text(encoding="utf-8"))
        values = [normalize_task_id(str(value)) for value in payload.get("task_ids", [])]
    values = list(dict.fromkeys(values))
    restricted_ids = [
        task_id for task_id in values
        if str(rows[task_id].get("license_gate", "none")) != "none"
    ]
    if restricted_ids and not args.allow_restricted_licenses:
        raise ValueError("restricted-license tasks require --allow-restricted-licenses")
    return values


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", action="append", help="Explicit task id; repeatable")
    parser.add_argument("--selection", default=None)
    parser.add_argument("--allow-restricted-licenses", action="store_true")
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--registry", default="docker.io/kevinxulearning")
    parser.add_argument("--tag", default="v0.1.0")
    parser.add_argument("--builder", default="desktop-linux")
    parser.add_argument(
        "--resume",
        action="store_true",
        help="skip tasks already marked dockerhub-published with both immutable digests",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.batch_size <= 0:
        raise ValueError("--batch-size must be positive")
    rows = {str(row["release_id"]): row for row in load_rows()}
    task_ids = selected_ids(args, rows)
    skipped: list[str] = []
    if args.resume:
        remaining: list[str] = []
        for task_id in task_ids:
            row = rows[task_id]
            if (
                row.get("status") == "dockerhub-published"
                and str(row.get("environment_image_digest") or "").startswith("sha256:")
                and str(row.get("verifier_image_digest") or "").startswith("sha256:")
            ):
                skipped.append(task_id)
            else:
                remaining.append(task_id)
        task_ids = remaining
    for task_id in task_ids:
        if task_id not in rows:
            raise ValueError(f"task {task_id} is absent from manifest")
        if not (ROOT / "tasks" / f"task_{task_id}" / "environment" / "Dockerfile").is_file():
            raise FileNotFoundError(f"missing environment context for {task_id}")
        if not (ROOT / "staging" / f"task_{task_id}" / "verifier" / "Dockerfile").is_file():
            raise FileNotFoundError(f"missing verifier context for {task_id}")

    print(json.dumps({"task_ids": task_ids, "skipped": skipped, "batch_size": args.batch_size, "registry": args.registry, "tag": args.tag}, indent=2))
    if args.dry_run:
        return 0
    ensure_builder(args.builder)
    publish_root = ROOT / "build" / "publish"
    for batch_number, start in enumerate(range(0, len(task_ids), args.batch_size), start=1):
        batch = task_ids[start : start + args.batch_size]
        batch_root = publish_root / f"batch-{batch_number:03d}"
        batch_root.mkdir(parents=True, exist_ok=True)
        references: list[str] = []
        print(json.dumps({"batch": batch_number, "task_ids": batch}, indent=2), flush=True)
        try:
            for task_id in batch:
                language = image_slug(str(rows[task_id].get("language") or "unknown"))
                env_ref = f"{args.registry}/swe-bench-science-environment-{language}-task-{task_id}:{args.tag}"
                verifier_ref = f"{args.registry}/swe-bench-science-verifier-{language}-task-{task_id}:{args.tag}"
                # Register both task references before starting either build;
                # cleanup remains effective even if build_push raises after a
                # successful local load or registry push.
                references.extend([env_ref, verifier_ref])
                env_digest = build_push(
                    builder=args.builder,
                    reference=env_ref,
                    dockerfile=ROOT / "tasks" / f"task_{task_id}" / "environment" / "Dockerfile",
                    context=ROOT / "tasks" / f"task_{task_id}" / "environment",
                    metadata_path=batch_root / f"task_{task_id}-environment.json",
                )
                verifier_digest = build_push(
                    builder=args.builder,
                    reference=verifier_ref,
                    dockerfile=ROOT / "staging" / f"task_{task_id}" / "verifier" / "Dockerfile",
                    context=ROOT / "staging" / f"task_{task_id}" / "verifier",
                    build_args=[f"BASE_IMAGE={env_ref}@{env_digest}"],
                    metadata_path=batch_root / f"task_{task_id}-verifier.json",
                )
                smoke_verifier(verifier_ref, task_id)
                env_image = f"{env_ref}@{env_digest}"
                verifier_image = f"{verifier_ref}@{verifier_digest}"
                update_manifest(task_id, env_ref=env_ref, env_digest=env_digest, verifier_ref=verifier_ref, verifier_digest=verifier_digest)
                update_task_bundle(task_id, env_image, verifier_image)
                print(json.dumps({"task_id": task_id, "environment": env_image, "verifier": verifier_image}, indent=2), flush=True)
        finally:
            cleanup_batch(args.builder, references)
    run(["python3", "scripts/generate_huggingface.py"])
    print(json.dumps({"published_tasks": len(task_ids), "batches": (len(task_ids) + args.batch_size - 1) // args.batch_size}, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"error: {exc}") from exc
