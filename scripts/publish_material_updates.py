#!/usr/bin/env python3
"""Patch audited material changes onto published amd64 task image pairs."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import shlex
import shutil
import subprocess
import time
from collections.abc import Sequence
from pathlib import Path

try:
    from material_policy import load_policies
    from build_publish_batch import apply_material_metadata, push_with_retry, write_rows
except ModuleNotFoundError:  # Imported as scripts.publish_material_updates in tests.
    from scripts.material_policy import load_policies
    from scripts.build_publish_batch import apply_material_metadata, push_with_retry, write_rows


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "manifests" / "tasks.jsonl"
PUBLISH_LOCK = ROOT / "build" / "publish.lock"
ID_RE = re.compile(r"^(?:task_)?(\d{1,3})$")


def normalize(value: str) -> str:
    match = ID_RE.fullmatch(value.strip())
    if not match:
        raise ValueError(f"invalid task id: {value!r}")
    task_id = f"{int(match.group(1)):03d}"
    if task_id == "120" or not 1 <= int(task_id) <= 119:
        raise ValueError(f"release task id must be 001..119: {value!r}")
    return task_id


def load_rows() -> list[dict[str, object]]:
    return [
        json.loads(line)
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def acquire_publish_lock():
    PUBLISH_LOCK.parent.mkdir(parents=True, exist_ok=True)
    handle = PUBLISH_LOCK.open("a+")
    if os.environ.get("SWE_BENCH_WAIT_FOR_PUBLISH_LOCK") == "1":
        print("+ waiting for the image-publisher lock", flush=True)
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX)
        return handle
    try:
        fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError as exc:
        handle.close()
        raise RuntimeError(
            "another image publisher is already updating this release; wait for it to finish"
        ) from exc
    return handle


def registry_env() -> dict[str, str]:
    env = os.environ.copy()
    if os.environ.get("SWE_BENCH_REGISTRY_PROXY") == "1":
        for name in (
            "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY",
            "http_proxy", "https_proxy", "all_proxy",
        ):
            if env.get(name):
                env[name] = env[name].replace("host.docker.internal", "127.0.0.1")
        return env
    for name in (
        "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY",
        "http_proxy", "https_proxy", "all_proxy",
    ):
        env.pop(name, None)
    return env


def run(command: list[str], *, capture: bool = False, registry: bool = False) -> str:
    print("+ " + " ".join(command), flush=True)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=registry_env() if registry else os.environ.copy(),
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
    )
    return (completed.stdout or "").strip()


def retry_registry(command: list[str], *, attempts: int = 4) -> str:
    for attempt in range(1, attempts + 1):
        try:
            return run(command, capture=True, registry=True)
        except subprocess.CalledProcessError as exc:
            if attempt == attempts:
                raise
            print(f"! registry attempt {attempt}/{attempts} failed: {(exc.stdout or '')[-800:]}", flush=True)
            time.sleep(5 * attempt)
    raise AssertionError("unreachable")


def container_path(task_id: str, relative: str) -> str:
    public_prefix = "environment/public/"
    source_prefix = "environment/repo/"
    if relative.startswith(public_prefix):
        return f"/app/task_{task_id}/{relative.removeprefix(public_prefix)}"
    if relative.startswith(source_prefix):
        return f"/app/task_{task_id}/source/{relative.removeprefix(source_prefix)}"
    raise ValueError(f"unsupported material policy path: {relative}")


def prepare_context(
    task_id: str,
    context: Path,
    policy: dict[str, object],
    *,
    verifier: bool = False,
) -> None:
    task_dir = ROOT / "tasks" / f"task_{task_id}"
    if context.exists():
        shutil.rmtree(context)
    public_overlay = context / "public_overlay"
    shutil.copytree(task_dir / "environment" / "public", public_overlay)

    source_paths = {
        str(destination).removeprefix("environment/repo/")
        for destination in dict(policy.get("overrides", {}))
        if str(destination).startswith("environment/repo/")
    }
    source_paths.update(
        str(relative).removeprefix("environment/repo/")
        for relative in policy.get("strip_notebook_outputs", [])
        if str(relative).startswith("environment/repo/")
    )
    for relative in sorted(source_paths):
        source = task_dir / "environment" / "repo" / relative
        if not source.is_file():
            raise FileNotFoundError(source)
        destination = context / "source_overlay" / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    removals = [
        container_path(task_id, str(relative))
        for relative in policy.get("remove", [])
    ]
    removal_command = "true"
    if removals:
        removal_command = "rm -rf " + " ".join(shlex.quote(path) for path in removals)
    dockerfile = [
        "ARG BASE_IMAGE",
        "FROM ${BASE_IMAGE}",
        f"RUN {removal_command}",
        f"COPY public_overlay/ /app/task_{task_id}/",
    ]
    if source_paths:
        dockerfile.append(f"COPY source_overlay/ /app/task_{task_id}/source/")
    verifier_overlay = ROOT / "staging" / f"task_{task_id}" / "verifier_release"
    if verifier and verifier_overlay.is_dir():
        shutil.copytree(verifier_overlay, context / "verifier_overlay")
        dockerfile.extend(
            [
                "RUN rm -rf /tests/private_tests",
                "COPY verifier_overlay/ /tests/",
                "RUN chmod 755 /tests/test.sh /tests/grader.py",
            ]
        )
    dockerfile.extend(
        [
            f"WORKDIR /app/task_{task_id}",
            "RUN git config user.email science-bench@example.invalid \\",
            "    && git config user.name 'SWE-bench Science baseline' \\",
            "    && git add -A \\",
            "    && GIT_AUTHOR_DATE=2025-01-01T00:00:00Z GIT_COMMITTER_DATE=2025-01-01T00:00:00Z git commit --amend --no-edit \\",
            "    && git reflog expire --expire=now --all \\",
            "    && git gc --prune=now",
        ]
    )
    (context / "Dockerfile").write_text("\n".join(dockerfile) + "\n", encoding="utf-8")


def build_layer_image(builder: str, base: str, reference: str, context: Path) -> None:
    run(
        [
            "docker", "buildx", "build", "--builder", builder,
            "--platform", "linux/amd64", "--pull=false", "--provenance=false",
            "--sbom=false", "--load", "--build-arg", f"BASE_IMAGE={base}",
            "--tag", reference, "--file", str(context / "Dockerfile"), str(context),
        ]
    )
    platform = run(
        ["docker", "image", "inspect", "--format", "{{.Os}}/{{.Architecture}}", reference],
        capture=True,
    )
    if platform != "linux/amd64":
        raise RuntimeError(f"patched image is not linux/amd64: {reference} -> {platform}")


def build_clean_image(
    builder: str,
    reference: str,
    dockerfile: Path,
    context: Path,
    *,
    build_args: Sequence[str] = (),
) -> None:
    command = [
        "docker", "buildx", "build", "--builder", builder,
        "--platform", "linux/amd64", "--pull=false", "--provenance=false",
        "--sbom=false", "--load", "--tag", reference,
    ]
    for build_arg in build_args:
        command.extend(["--build-arg", build_arg])
    command.extend(["--file", str(dockerfile), str(context)])
    run(command)
    platform = run(
        ["docker", "image", "inspect", "--format", "{{.Os}}/{{.Architecture}}", reference],
        capture=True,
    )
    if platform != "linux/amd64":
        raise RuntimeError(f"clean image is not linux/amd64: {reference} -> {platform}")


def reusable_local_image(reference: str) -> bool:
    probe = subprocess.run(
        ["docker", "image", "inspect", reference],
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    if probe.returncode != 0:
        return False
    platform = run(
        ["docker", "image", "inspect", "--format", "{{.Os}}/{{.Architecture}}", reference],
        capture=True,
    )
    if platform != "linux/amd64":
        raise RuntimeError(f"local image is not linux/amd64: {reference} -> {platform}")
    return True


def requires_clean_rebuild(policy: dict[str, object]) -> bool:
    """Return true when an old layer could retain excluded or modified bytes."""
    return any(
        policy.get(key)
        for key in (
            "remove", "remove_globs", "retain_files", "retain_subdirectories",
            "strip_notebook_outputs",
        )
    )


def publish_clean_pair(
    *,
    builder: str,
    task_id: str,
    policy: dict[str, object],
    env_ref: str,
    verifier_ref: str,
    verifier_context: Path,
    reuse_local_images: bool = False,
) -> tuple[str, str]:
    """Build, validate, and push a pair from the audited clean contexts."""
    environment_source = ROOT / "tasks" / f"task_{task_id}" / "environment"
    prepare_clean_verifier_context(task_id, verifier_context)
    if not (reuse_local_images and reusable_local_image(env_ref)):
        build_clean_image(
            builder,
            env_ref,
            environment_source / "Dockerfile",
            environment_source,
        )
    else:
        print(f"+ task {task_id}: reusing local environment image; validating before push", flush=True)
    validate_image(task_id, env_ref, policy)
    validate_public_reproduction(task_id, env_ref)
    env_digest = push(env_ref)
    if not (reuse_local_images and reusable_local_image(verifier_ref)):
        build_clean_image(
            builder,
            verifier_ref,
            verifier_context / "Dockerfile",
            verifier_context,
            build_args=[f"BASE_IMAGE={env_ref}@{env_digest}"],
        )
    else:
        print(f"+ task {task_id}: reusing local verifier image; validating before push", flush=True)
    validate_image(task_id, verifier_ref, policy, verifier=True)
    verifier_digest = push(verifier_ref)
    return env_digest, verifier_digest


def prepare_clean_verifier_context(task_id: str, context: Path) -> None:
    source = ROOT / "staging" / f"task_{task_id}" / "verifier"
    if not source.is_dir():
        raise FileNotFoundError(source)
    if context.exists():
        shutil.rmtree(context)
    shutil.copytree(source, context)

    release_overlay = ROOT / "staging" / f"task_{task_id}" / "verifier_release"
    if not release_overlay.is_dir():
        return
    private_tests = context / "private_tests"
    if private_tests.exists():
        shutil.rmtree(private_tests)
    shutil.copytree(release_overlay, context, dirs_exist_ok=True)


def validate_image(
    task_id: str,
    reference: str,
    policy: dict[str, object],
    *,
    verifier: bool = False,
) -> None:
    checks = [
        f"test -f /app/task_{task_id}/MATERIALS.json",
        f"test -f /app/task_{task_id}/MATERIALS_LICENSES.md",
    ]
    checks.extend(
        f"test ! -e {shlex.quote(container_path(task_id, str(relative)))}"
        for relative in policy.get("remove", [])
    )
    run(["docker", "run", "--rm", "--entrypoint", "sh", reference, "-c", " && ".join(checks)])
    if verifier and task_id == "032":
        run(
            [
                "docker", "run", "--rm", "--entrypoint", "sh", reference, "-c",
                "test -f /tests/private_tests/test_task_032.py && "
                "test \"$(find /tests/private_tests -type f -name 'test_*.py' | wc -l)\" -eq 1 && "
                "test -z \"$(find /tests -iname '*apgr*' -print -quit)\"",
            ]
        )
    if policy.get("strip_notebook_outputs"):
        notebook_paths = [
            container_path(task_id, str(relative))
            for relative in policy.get("strip_notebook_outputs", [])
        ]
        code = (
            "import json,sys,pathlib; "
            "bad=[p for p in sys.argv[1:] if (lambda nb: "
            "any(c.get('cell_type')=='code' and (c.get('outputs') or "
            "c.get('execution_count') is not None) for c in nb.get('cells',[])) "
            "or 'widgets' in nb.get('metadata',{}))"
            "(json.loads(pathlib.Path(p).read_text()))]; "
            "raise SystemExit('notebook execution state remains: '+','.join(bad) if bad else 0)"
        )
        run(["docker", "run", "--rm", "--entrypoint", "python", reference, "-c", code, *notebook_paths])


def validate_public_reproduction(task_id: str, reference: str) -> None:
    command = [
        "docker", "run", "--rm", "--network", "none",
        "--entrypoint", "python", reference, "reproduce.py",
    ]
    print("+ " + " ".join(command), flush=True)
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
            timeout=1800,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"public reproduction timed out for task {task_id}") from exc
    output = completed.stdout or ""
    print(output[-4000:], flush=True)
    if completed.returncode not in {0, 1}:
        raise RuntimeError(
            f"public reproduction failed as infrastructure for task {task_id}: "
            f"exit {completed.returncode}"
        )
    if task_id == "032" and completed.returncode != 1:
        raise RuntimeError("task 032 baseline must reproduce the pre-fix mismatch")


def push(reference: str) -> str:
    output = push_with_retry(reference, attempts=4)
    match = re.search(r"digest:\s*(sha256:[0-9a-f]{64})", output)
    if not match:
        raise RuntimeError(f"docker push returned no digest for {reference}: {output}")
    return match.group(1)


def update_manifest(
    task_id: str,
    *,
    env_ref: str,
    env_digest: str,
    verifier_ref: str,
    verifier_digest: str,
) -> None:
    rows = load_rows()
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
        raise ValueError(f"task {task_id} is absent from manifest")
    MANIFEST.write_text(
        "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows),
        encoding="utf-8",
    )


def update_task_bundle(task_id: str, env_image: str, verifier_image: str) -> None:
    task_dir = ROOT / "tasks" / f"task_{task_id}"
    task_toml = task_dir / "task.toml"
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
    text = tests_dockerfile.read_text(encoding="utf-8")
    tests_dockerfile.write_text(
        re.sub(r"ARG VERIFIER_IMAGE=.*", f"ARG VERIFIER_IMAGE={verifier_image}", text, count=1),
        encoding="utf-8",
    )


def cleanup(builder: str, references: list[str]) -> None:
    for reference in dict.fromkeys(references):
        subprocess.run(["docker", "image", "rm", "-f", reference], cwd=ROOT, check=False)
    subprocess.run(["docker", "image", "prune", "--force"], cwd=ROOT, check=False)
    subprocess.run(["docker", "buildx", "prune", "--builder", builder, "--force"], cwd=ROOT, check=False)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--task-id", action="append", required=True)
    parser.add_argument("--allow-restricted-licenses", action="store_true")
    parser.add_argument("--registry", default="docker.io/kevinxulearning")
    parser.add_argument("--tag", default="v0.1.1")
    parser.add_argument("--batch-size", type=int, default=10)
    parser.add_argument("--builder", default="desktop-linux")
    parser.add_argument(
        "--force-clean-rebuild",
        action="store_true",
        help="rebuild every selected image pair from its current clean context",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="skip selected tasks already published with the requested tag and digests",
    )
    parser.add_argument(
        "--reuse-local-images",
        action="store_true",
        help="resume a failed push from a validated local amd64 image when available",
    )
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    publish_lock = acquire_publish_lock()
    if args.batch_size <= 0:
        raise ValueError("--batch-size must be positive")
    task_ids = list(dict.fromkeys(normalize(value) for value in args.task_id))
    policies = load_policies()
    rows = {str(row["release_id"]): row for row in load_rows()}
    for task_id in task_ids:
        if task_id not in policies:
            raise ValueError(f"task {task_id} has no audited material policy")
        if str(rows[task_id].get("license_gate", "none")) != "none" and not args.allow_restricted_licenses:
            raise ValueError(f"task {task_id} requires --allow-restricted-licenses")
        if task_id == "032" and not (
            ROOT / "staging" / "task_032" / "verifier_release" / "private_tests" / "test_task_032.py"
        ).is_file():
            raise ValueError(
                "task 032 requires its maintainer-only synthetic verifier overlay"
            )
        apply_material_metadata(task_id, rows[task_id])
    skipped: list[str] = []
    if args.resume:
        remaining: list[str] = []
        for task_id in task_ids:
            row = rows[task_id]
            if (
                str(row.get("status")) == "dockerhub-published"
                and str(row.get("environment_image_tag", "")).endswith(f":{args.tag}")
                and str(row.get("verifier_image_tag", "")).endswith(f":{args.tag}")
                and str(row.get("environment_image_digest", "")).startswith("sha256:")
                and str(row.get("verifier_image_digest", "")).startswith("sha256:")
            ):
                skipped.append(task_id)
            else:
                remaining.append(task_id)
        task_ids = remaining
    write_rows(list(rows.values()))
    print(
        json.dumps(
            {
                "task_ids": task_ids,
                "tag": args.tag,
                "batch_size": args.batch_size,
                "force_clean_rebuild": args.force_clean_rebuild,
                "reuse_local_images": args.reuse_local_images,
                "skipped": skipped,
            },
            indent=2,
        )
    )
    if args.dry_run:
        return 0

    run(["docker", "buildx", "inspect", "--builder", args.builder, "--bootstrap"])
    publish_root = ROOT / "build" / "material-updates"
    for batch_number, start in enumerate(range(0, len(task_ids), args.batch_size), start=1):
        batch = task_ids[start : start + args.batch_size]
        references: list[str] = []
        try:
            for task_id in batch:
                row = {str(item["release_id"]): item for item in load_rows()}[task_id]
                old_env = str(row.get("environment_image") or "")
                old_verifier = str(row.get("verifier_image") or "")
                language = re.sub(
                    r"[^a-z0-9]+", "-", str(row.get("language") or "unknown").lower()
                ).strip("-")
                env_ref = f"{args.registry}/swe-bench-science-environment-{language}-task-{task_id}:{args.tag}"
                verifier_ref = f"{args.registry}/swe-bench-science-verifier-{language}-task-{task_id}:{args.tag}"
                references.extend([env_ref, verifier_ref])
                task_context = publish_root / f"batch-{batch_number:03d}" / f"task_{task_id}"
                env_context = task_context / "environment"
                verifier_context = task_context / "verifier"
                policy = policies[task_id]
                if args.force_clean_rebuild or requires_clean_rebuild(policy):
                    print(f"+ task {task_id}: clean rebuild required", flush=True)
                    env_digest, verifier_digest = publish_clean_pair(
                        builder=args.builder,
                        task_id=task_id,
                        policy=policy,
                        env_ref=env_ref,
                        verifier_ref=verifier_ref,
                        verifier_context=verifier_context,
                        reuse_local_images=args.reuse_local_images,
                    )
                else:
                    if not old_env.startswith("docker.io/") or not old_verifier.startswith("docker.io/"):
                        raise ValueError(f"task {task_id} has no reusable Docker Hub image pair")
                    try:
                        retry_registry(["docker", "pull", "--platform", "linux/amd64", old_env])
                        retry_registry(["docker", "pull", "--platform", "linux/amd64", old_verifier])
                    except subprocess.CalledProcessError as exc:
                        print(
                            f"! task {task_id}: old image pull failed; falling back to clean rebuild: {exc}",
                            flush=True,
                        )
                        env_digest, verifier_digest = publish_clean_pair(
                            builder=args.builder,
                            task_id=task_id,
                            policy=policy,
                            env_ref=env_ref,
                            verifier_ref=verifier_ref,
                            verifier_context=verifier_context,
                        )
                    else:
                        references.extend([old_env, old_verifier])
                        prepare_context(task_id, env_context, policy)
                        prepare_context(task_id, verifier_context, policy, verifier=True)
                        build_layer_image(args.builder, old_env, env_ref, env_context)
                        validate_image(task_id, env_ref, policy)
                        validate_public_reproduction(task_id, env_ref)
                        env_digest = push(env_ref)
                        build_layer_image(args.builder, old_verifier, verifier_ref, verifier_context)
                        validate_image(task_id, verifier_ref, policy, verifier=True)
                        verifier_digest = push(verifier_ref)
                env_image = f"{env_ref}@{env_digest}"
                verifier_image = f"{verifier_ref}@{verifier_digest}"
                update_manifest(
                    task_id,
                    env_ref=env_ref,
                    env_digest=env_digest,
                    verifier_ref=verifier_ref,
                    verifier_digest=verifier_digest,
                )
                update_task_bundle(task_id, env_image, verifier_image)
                print(json.dumps({"task_id": task_id, "environment": env_image, "verifier": verifier_image}, indent=2), flush=True)
        finally:
            cleanup(args.builder, references)
    run(["python3", "scripts/generate_huggingface.py"])
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"error: {exc}") from exc
