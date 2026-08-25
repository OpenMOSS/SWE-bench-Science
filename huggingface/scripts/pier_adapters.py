#!/usr/bin/env python3
"""Small runtime-only Pier adapters shared by all task images."""

from __future__ import annotations

from pier.agents.installed.codex import Codex


class ScienceBenchCodex(Codex):
    """Use npm's optional platform package when Pier installs Codex."""

    def install_spec(self):
        spec = super().install_spec()
        for step in spec.steps:
            step.run = step.run.replace(
                "npm install -g @openai/codex",
                "npm install -g --include=optional @openai/codex",
            )
        return spec
