---
pretty_name: SWE-bench Science
language:
  - en
task_categories:
  - text-generation
tags:
  - software-engineering
  - code-agents
  - scientific-computing
  - benchmark
---

# SWE-bench Science

> Generated from the canonical 119-row release manifest. Image references remain
> blank until the Docker Hub namespace and immutable digests are supplied.

SWE-bench Science evaluates coding agents on software-engineering problems from
scientific computing repositories. Each task is paired with an isolated task
environment and a separate verifier environment. Agent harnesses are selected
at evaluation time through Pier and are not baked into per-task release images.

## Dataset Summary

| Metric | Value |
| --- | ---: |
| Total tasks | 119 |
| Default non-GPL-family tasks | 107 |
| GPL/LGPL/AGPL-family opt-in tasks | 12 |
| Task environment images | 1 local canary / 118 pending |
| Separate verifier images | 1 local canary / 118 pending |
| linux/amd64 coverage | pending |

Domain, language, license, and verifier-status tables will be generated from
`data/tasks.csv`; they will not be maintained manually. `UNKNOWN` is retained
when a sparse upstream source has no machine-detectable license; such rows need
manual review before final publication.

## Task Format

Each row records a stable task id, title, scientific domain, implementation
language, upstream repository and base commit, source license, GPL-family gate,
task environment image, verifier image, and local Pier task path.

The downloadable task bundle follows the Harbor-compatible format consumed by
Pier. The task environment and verifier run in separate containers. A trial
exports the agent's Git diff as `model.patch`; the verifier applies it to a
fresh baseline, rebuilds the project, and runs the grading contract offline.

Pier currently runs local task directories rather than downloading this Hugging
Face dataset directly. The release therefore includes a small materialization
tool that resolves an explicit selection into a local `tasks-selected/`
directory before `pier run -p tasks-selected`.

## Quick Start

After the image columns contain final Docker Hub digests, a clean user can run:

```bash
python3 -m pip install "huggingface_hub[cli]"
hf auth login
hf download <organization>/<dataset-repo> \
  --repo-type dataset --local-dir swe-bench-science
cd swe-bench-science

uv venv --python 3.12 .venv
uv pip install "git+https://github.com/datacurve-ai/pier.git"

# Default: the fixed 107-task non-GPL selection.
python3 tools/materialize.py --output tasks-selected

# Arbitrary explicit batch. A GPL-family id still requires --allow-GPL.
python3 tools/materialize.py --task-id 002 --task-id 019 \
  --output tasks-selected-small

# Pull both prebuilt images per task as linux/amd64, then run Pier.
python3 tools/run_batch.py --path tasks-selected-small \
  --pier-bin .venv/bin/pier --agent nop --n-concurrent 2
```

To materialize all tasks, including the 12 GPL-family tasks:

```bash
python3 tools/materialize.py --allow-GPL --output tasks-selected-all
```

The materializer writes the exact task ids to `selection.json`. The batch runner
hashes that list, pulls the environment and verifier images, writes a redacted
`batch-run.json`, and invokes Pier with `--no-force-build --no-delete`. It never
uses runner-side random sampling.

## Codex Gateway Profile

Keep credentials outside the dataset checkout. Start from
`profiles/codex.env.example`, place the real profile in a user-only directory,
and select it per run:

```bash
python3 tools/run_batch.py --path tasks-selected-small \
  --pier-bin .venv/bin/pier --agent codex \
  --env-file ~/.config/swe-bench-science/openai.env \
  --n-concurrent 2 --n-attempts 1
```

| Field | Purpose |
| --- | --- |
| `MODEL` | Model sent to Codex; CLI `--model` overrides it |
| `OPENAI_API_KEY` | Gateway credential; never written to run metadata |
| `CODEX_BASE_URL` | Selected relay or OpenAI-compatible endpoint |
| `CODEX_WIRE_API` | `responses` or `chat` |
| `CODEX_VERSION` | Installed `@openai/codex` version |
| `CODEX_REASONING_EFFORT` | Codex reasoning effort |

The runner translates these fields into Pier's native Codex `config_toml` and
derives the network allowlist from the endpoint. Switching relay, protocol, or
credential means selecting another env file; task files and images do not
change. Advanced users can disable this translation with `--no-auto-provider`
and pass repeated `--agent-kwarg` / `--agent-env` values directly to Pier.
For a short smoke, add `--agent-timeout-multiplier 0.0223` (approximately 120
seconds against the default task timeout); verifier timeout remains separate.

## Agent Harnesses

Codex, Claude Code, mini-swe-agent, and other Pier-supported harnesses are trial
configuration. They are not dataset columns and are not published once per
task. Reproducible evaluation records pin the Pier version, agent/version,
model/provider configuration, installation fingerprint, and both image digests.

## GPL-family Tasks

The default download selection contains 107 tasks. Use the project download
tool's explicit `--allow-GPL` option to materialize all 119 tasks. This option
is a distribution selection and does not replace compliance with the upstream
license of each source repository.

## Security and Leakage Policy

The dataset does not distribute reference-answer patches, oracle solutions,
author notes, credentials, or previous agent trajectories. Verifier material is
never mounted into the agent environment. The verifier disclosure policy is
pending final confirmation by the dataset owners.

## Images

Image references will point to immutable Docker Hub digests after the owners
provide the final namespace and complete per-task validation. Blank image fields
mean unpublished, not "use a default image".

## Citation

Pending the final paper citation.

## License

Dataset metadata license: pending owner confirmation. Each task row records the
license of its upstream source repository separately.
