#!/usr/bin/env python3
"""Pull prebuilt task images and run an explicit local selection with Pier."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shlex
import subprocess
import sys
from pathlib import Path

try:
    from .provider_config import parse_dotenv, render_codex_config, resolve_codex_profile
except ImportError:  # Direct execution: python3 scripts/run_batch.py
    from provider_config import parse_dotenv, render_codex_config, resolve_codex_profile

try:
    from .summarize_results import write_summary
except ImportError:  # Direct execution: python3 scripts/run_batch.py
    from summarize_results import write_summary

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 and earlier
    try:
        import tomli as tomllib
    except ModuleNotFoundError as exc:  # pragma: no cover - depends on host Python
        raise SystemExit(
            "run_batch.py requires Python 3.11+ or the backport: "
            "python3 -m pip install tomli"
        ) from exc


def task_dirs(root: Path) -> list[Path]:
    if root.name.startswith("task_") and (root / "task.toml").is_file():
        return [root]
    return sorted(
        (path for path in root.glob("task_*") if path.is_dir()),
        key=lambda path: path.name,
    )


def validate_artifact_hooks(task_dirs_: list[Path]) -> None:
    missing = [
        task_dir.name
        for task_dir in task_dirs_
        if not (task_dir / "pre_artifacts.sh").is_file()
    ]
    if missing:
        raise ValueError(
            "task bundles are missing pre_artifacts.sh; rematerialize them with "
            "the current release tools: " + ", ".join(missing)
        )


def load_image_refs(task_dir: Path) -> list[str]:
    config = tomllib.loads((task_dir / "task.toml").read_text(encoding="utf-8"))
    refs = [
        config.get("environment", {}).get("docker_image", ""),
        config.get("verifier", {}).get("environment", {}).get("docker_image", ""),
    ]
    missing = [ref for ref in refs if not ref or "pending" in ref]
    if missing:
        raise ValueError(f"{task_dir.name} has unpublished image references")
    return list(dict.fromkeys(refs))


def pull_images(task_dirs_: list[Path], *, platform: str) -> list[str]:
    refs: list[str] = []
    for task_dir in task_dirs_:
        refs.extend(load_image_refs(task_dir))
    refs = list(dict.fromkeys(refs))
    for ref in refs:
        command = ["docker", "pull", "--platform", platform, ref]
        print("+ " + shlex.join(command), flush=True)
        subprocess.run(command, check=True)
    return refs


def selection_payload(root: Path, dirs: list[Path]) -> dict[str, object]:
    selection_file = root / "selection.json"
    if selection_file.is_file():
        payload = json.loads(selection_file.read_text(encoding="utf-8"))
        task_ids = [str(value) for value in payload.get("task_ids", [])]
    else:
        task_ids = [path.name.removeprefix("task_") for path in dirs]
        payload = {
            "allow_restricted_licenses": None,
            "task_ids": task_ids,
        }
    canonical = json.dumps({"task_ids": task_ids}, sort_keys=True).encode("utf-8")
    payload["task_ids"] = task_ids
    payload["selection_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def redacted_command(command: list[str]) -> str:
    redacted: list[str] = []
    index = 0
    while index < len(command):
        value = command[index]
        if value == "--agent-env" and index + 1 < len(command):
            redacted.extend([value, "<redacted>"])
            index += 2
            continue
        if (
            value == "--agent-kwarg"
            and index + 1 < len(command)
            and command[index + 1].startswith("config_toml=")
        ):
            redacted.extend([value, "config_toml=<provider-config>"])
            index += 2
            continue
        if "=" in value:
            key = value.split("=", 1)[0].lower()
            if any(marker in key for marker in ("key", "token", "secret", "password", "authorization")):
                redacted.append(key + "=<redacted>")
                index += 1
                continue
        redacted.append(value)
        index += 1
    return shlex.join(redacted)


def pier_version(pier_bin: str) -> str | None:
    try:
        completed = subprocess.run(
            [pier_bin, "--version"], capture_output=True, text=True, check=False
        )
    except OSError:
        return None
    value = (completed.stdout or completed.stderr).strip()
    return value or None


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog="Use docs/run-batch.md for provider profiles, gateway routing, and result paths.",
    )
    parser.add_argument("--path", type=Path, required=True, help="Materialized task directory")
    parser.add_argument("--agent", default="nop", help="Pier harness, for example codex, claude-code, mini-swe-agent, or nop")
    parser.add_argument("--env", default="docker", help="Pier environment backend")
    parser.add_argument("--env-file", type=Path, help="Provider/harness dotenv file")
    parser.add_argument("--model", action="append", default=[], help="Model route; repeatable")
    parser.add_argument("--agent-env", action="append", default=[], help="Extra harness environment KEY=VALUE; repeatable")
    parser.add_argument("--agent-kwarg", action="append", default=[], help="Extra Pier agent keyword KEY=VALUE; repeatable")
    parser.add_argument("--n-concurrent", type=int, default=1, help="Simultaneous tasks (default: 1)")
    parser.add_argument("--n-attempts", type=int, default=1, help="Attempts per task (default: 1)")
    parser.add_argument("--max-retries", type=int, default=0, help="Retries after attempt-level failure (default: 0)")
    parser.add_argument("--agent-timeout-multiplier", type=float, help="Multiplier for the agent-stage timeout")
    parser.add_argument("--verifier-timeout-multiplier", type=float, help="Multiplier for verifier/build timeouts")
    parser.add_argument("--jobs-dir", type=Path, default=Path("jobs"), help="Pier jobs and summary directory")
    parser.add_argument("--job-name", help="Stable name used in result paths")
    parser.add_argument("--platform", default="linux/amd64", help="Docker platform (default: linux/amd64)")
    parser.add_argument("--pier-bin", default="pier", help="Pier executable or absolute path")
    parser.add_argument("--agent-import-path", help="Explicit Pier agent import path")
    parser.add_argument("--skip-pull", action="store_true", help="Skip Docker pulls for refs already present locally")
    parser.add_argument(
        "--no-auto-provider",
        action="store_true",
        help="Do not translate CODEX_* values from --env-file into native Pier kwargs",
    )
    parser.add_argument(
        "--no-auto-agent-adapter",
        action="store_true",
        help="Use Pier's built-in agent class instead of the runtime-only Codex adapter",
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate, pull, and record metadata without invoking Pier")
    args = parser.parse_args()

    root = args.path.resolve()
    dirs = task_dirs(root)
    if not dirs:
        raise ValueError(f"no task_NNN directories found under {root}")
    validate_artifact_hooks(dirs)
    selection = selection_payload(root, dirs)
    image_refs: list[str] = []
    for task_dir in dirs:
        image_refs.extend(load_image_refs(task_dir))
    image_refs = list(dict.fromkeys(image_refs))
    if not args.skip_pull:
        pull_images(dirs, platform=args.platform)
    models = list(args.model)
    agent_kwargs = list(args.agent_kwarg)
    agent_import_path = args.agent_import_path
    if args.agent == "codex" and not args.no_auto_agent_adapter and not agent_import_path:
        package = Path(__file__).resolve().parent.name
        agent_import_path = f"{package}.pier_adapters:ScienceBenchCodex"
    provider_metadata: dict[str, object] | None = None
    if args.agent == "codex" and not args.no_auto_provider:
        profile_env = dict(os.environ)
        if args.env_file:
            profile_env.update(parse_dotenv(args.env_file))
        profile = resolve_codex_profile(profile_env)
        if not models:
            models.append(profile.model)
        if not any(value.startswith(("config_toml=", "config_toml_file=")) for value in agent_kwargs):
            agent_kwargs.append("config_toml=" + render_codex_config(profile))
        # Pier normally strips a provider prefix before invoking Codex. Gateways
        # may use that prefix for routing, so preserve the exact model identifier
        # unless the caller supplied an explicit command override.
        if not any(value.startswith("command_model_name=") for value in agent_kwargs):
            agent_kwargs.append("command_model_name=" + profile.model)
        if profile.version and not any(value.startswith("version=") for value in agent_kwargs):
            agent_kwargs.append("version=" + profile.version)
        if profile.reasoning_effort and not any(
            value.startswith("reasoning_effort=") for value in agent_kwargs
        ):
            agent_kwargs.append("reasoning_effort=" + profile.reasoning_effort)
        provider_metadata = {
            "protocol": profile.wire_api,
            "base_url": profile.safe_base_url,
            "credential_env": "OPENAI_API_KEY",
        }

    command = [
        args.pier_bin, "run", "--path", str(root), "--agent", args.agent, "--env", args.env,
        "--n-concurrent", str(args.n_concurrent), "--n-attempts", str(args.n_attempts),
        "--max-retries", str(args.max_retries), "--no-force-build", "--no-delete", "--yes",
    ]
    if args.agent_timeout_multiplier is not None:
        command.extend(["--agent-timeout-multiplier", str(args.agent_timeout_multiplier)])
    if args.verifier_timeout_multiplier is not None:
        command.extend(["--verifier-timeout-multiplier", str(args.verifier_timeout_multiplier)])
    if args.env_file:
        command.extend(["--env-file", str(args.env_file)])
    if agent_import_path:
        command.extend(["--agent-import-path", agent_import_path])
    for model in models:
        command.extend(["--model", model])
    for value in args.agent_env:
        command.extend(["--agent-env", value])
    for value in agent_kwargs:
        command.extend(["--agent-kwarg", value])
    if args.jobs_dir:
        command.extend(["--jobs-dir", str(args.jobs_dir)])
    if args.job_name:
        command.extend(["--job-name", args.job_name])

    metadata = {
        "task_ids": selection["task_ids"],
        "allow_restricted_licenses": selection.get("allow_restricted_licenses"),
        "selection_sha256": selection["selection_sha256"],
        "image_refs": image_refs,
        "platform": args.platform,
        "agent": args.agent,
        "models": models,
        "n_concurrent": args.n_concurrent,
        "n_attempts": args.n_attempts,
        "max_retries": args.max_retries,
        "pier_version": pier_version(args.pier_bin),
        "pier_command": redacted_command(command),
        "agent_import_path": agent_import_path,
        "provider": provider_metadata,
    }
    metadata_path = root / "batch-run.json"
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(metadata, indent=2, sort_keys=True))
    if args.dry_run:
        return 0
    pier_environment = os.environ.copy()
    # Pier may build an ephemeral environment+agent image. Keep that derived
    # build on the same architecture as the prebuilt task images.
    pier_environment["DOCKER_DEFAULT_PLATFORM"] = args.platform
    tool_root = str(Path(__file__).resolve().parent.parent)
    existing_pythonpath = pier_environment.get("PYTHONPATH", "")
    pier_environment["PYTHONPATH"] = os.pathsep.join(
        value for value in (tool_root, existing_pythonpath) if value
    )
    returncode = subprocess.run(command, check=False, env=pier_environment).returncode
    try:
        summary_json, summary_csv = write_summary(args.jobs_dir)
        print(json.dumps({"summary_json": str(summary_json), "summary_csv": str(summary_csv)}, indent=2))
    except (OSError, ValueError) as exc:
        print(f"warning: unable to write result summary: {exc}", file=sys.stderr)
    return returncode


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError, tomllib.TOMLDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
