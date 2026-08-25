#!/usr/bin/env python3
"""Resolve a Codex gateway profile without persisting credential values."""

from __future__ import annotations

import json
import shlex
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


@dataclass(frozen=True)
class CodexProfile:
    model: str
    base_url: str
    wire_api: str
    version: str | None
    reasoning_effort: str | None

    @property
    def safe_base_url(self) -> str:
        parts = urlsplit(self.base_url)
        host = parts.hostname or ""
        if parts.port:
            host = f"{host}:{parts.port}"
        return urlunsplit((parts.scheme, host, parts.path, "", ""))


def parse_dotenv(path: Path) -> dict[str, str]:
    if not path.is_file():
        raise FileNotFoundError(path)
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        if text.startswith("export "):
            text = text[7:].lstrip()
        if "=" not in text:
            continue
        key, value = text.split("=", 1)
        key = key.strip()
        if not key or not key.replace("_", "").isalnum() or key[0].isdigit():
            continue
        value = value.strip()
        if value and value[0] in "\"'" and value[-1:] == value[0]:
            parts = shlex.split(value, comments=False, posix=True)
            value = parts[0] if parts else ""
        elif " #" in value:
            value = value.split(" #", 1)[0].rstrip()
        values[key] = value
    return values


def resolve_codex_profile(environ: Mapping[str, str]) -> CodexProfile:
    wire = environ.get("CODEX_WIRE_API", "responses").strip().lower().replace("-", "_")
    aliases = {
        "responses": "responses",
        "openai_responses": "responses",
        "chat": "chat",
        "openai_chat": "chat",
    }
    if wire not in aliases:
        raise ValueError("CODEX_WIRE_API must be responses or chat")
    base_url = (
        environ.get("CODEX_BASE_URL")
        or environ.get("OPENAI_BASE_URL")
        or "https://api.openai.com/v1"
    ).strip()
    parts = urlsplit(base_url)
    if parts.scheme not in {"http", "https"} or not parts.hostname:
        raise ValueError("CODEX_BASE_URL must be an http(s) URL")
    return CodexProfile(
        model=(environ.get("MODEL") or "gpt-5").strip(),
        base_url=base_url,
        wire_api=aliases[wire],
        version=(environ.get("CODEX_VERSION") or "").strip() or None,
        reasoning_effort=(
            environ.get("CODEX_REASONING_EFFORT")
            or environ.get("REASONING_EFFORT")
            or ""
        ).strip()
        or None,
    )


def render_codex_config(profile: CodexProfile) -> str:
    return "\n".join(
        [
            'model_provider = "science_bench_gateway"',
            "",
            "[model_providers.science_bench_gateway]",
            'name = "SWE-bench Science Gateway"',
            f"base_url = {json.dumps(profile.base_url)}",
            f"wire_api = {json.dumps(profile.wire_api)}",
            'env_key = "OPENAI_API_KEY"',
            "",
        ]
    )
