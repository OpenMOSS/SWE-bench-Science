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
license: mit
---

# SWE-bench Science

SWE-bench Science evaluates coding agents on software-engineering problems from
scientific computing repositories. The release contains 119 tasks. Each task
has an isolated environment image and a separate verifier image, both pinned to
immutable `linux/amd64` Docker Hub digests.

## Dataset Summary

| Metric | Value |
| --- | ---: |
| Total tasks | 119 |
| Default unrestricted-license tasks | 100 |
| Restricted-license opt-in tasks | 19 |
| GPL/LGPL/AGPL-family tasks | 18 |
| Task environment images | 119 Docker Hub digests |
| Separate verifier images | 119 Docker Hub digests |
| `linux/amd64` coverage | 119/119 |

The complete generated tables are in [`data/tasks.csv`](data/tasks.csv) and
[`data/statistics.md`](data/statistics.md). License values are recorded from
the upstream repository, source metadata, or source file headers; non-SPDX
family labels are kept explicit when a project does not use a standard SPDX id.

## What Is In The Dataset

The snapshot contains the task table, statistics, fixed selections, thin
Harbor/Pier task bundles, and the helper tools under `tools/`. It does not
contain reference-answer patches, credentials, agent trajectories, or private
verifier tests. The environment image contains the baseline source and public
dependencies. The verifier image contains held-out tests and the grader.

Pier installs the selected agent harness at evaluation time. Codex, Claude Code,
mini-swe-agent, and other Pier-supported agents are evaluation configuration,
not per-task image variants.

## Quick Start

```bash
python3 -m pip install "huggingface_hub[cli]"
hf auth login
hf download OpenMOSS-Team/SWE-bench-Science \
  --repo-type dataset --local-dir swe-bench-science
cd swe-bench-science

uv tool install "datacurve-pier==0.3.0"
# Without uv: python3 -m pip install "datacurve-pier==0.3.0"
docker login
```

Materialize the default 100-task selection:

```bash
python3 tools/materialize.py --output tasks-selected --force
```

Materialize a specific list, including inclusive ranges:

```bash
python3 tools/materialize.py \
  --task-id 002,005-007 \
  --output tasks-selected-small --force
```

Restricted-license tasks require an explicit gate. This includes GPL-family
tasks and task 019, whose upstream license is academic non-commercial:

```bash
python3 tools/materialize.py \
  --allow-restricted-licenses \
  --output tasks-selected-all --force
```

The 18 GPL-family ids are `003, 020, 021, 023, 032, 057, 066, 074, 075, 082,
083, 084, 085, 096, 097, 098, 100, 118`. Task `019` uses an academic
non-commercial license. All 19 ids require `--allow-restricted-licenses`.
The materializer records the exact result in `selection.json`.

## Run An Evaluation

Install Pier and run a no-op infrastructure smoke:

```bash
pier run -p tasks-selected-small \
  --agent nop --env docker --n-concurrent 1 \
  --no-force-build --no-delete --yes
```

Run Claude Code, Codex, or mini-swe-agent by changing only the harness, model,
and provider profile:

```bash
# Claude Code
pier run -p tasks-selected-small --agent claude-code --env docker \
  --env-file ~/.config/swe-bench-science/claude.env \
  --model anthropic/claude-opus-4-7 --n-concurrent 1

# mini-swe-agent
pier run -p tasks-selected-small --agent mini-swe-agent --env docker \
  --env-file ~/.config/swe-bench-science/mini-swe-agent.env \
  --model openai/gpt-5 --n-concurrent 1
```

The repository also provides an optional wrapper that pre-pulls every immutable
image and writes a flat summary:

```bash
python3 tools/run_batch.py \
  --path tasks-selected-small \
  --agent codex \
  --env-file ~/.config/swe-bench-science/codex.env \
  --n-concurrent 2 --n-attempts 1 \
  --jobs-dir jobs --job-name codex-small
```

For a short agent smoke, add
`--agent-timeout-multiplier 0.0223` (approximately 120 seconds against the
default task timeout). This only limits the agent stage; scientific verifier
builds and tests retain their own timeout.

## Provider Profiles

The examples in [`profiles/`](profiles/) are templates only. Copy them outside
the checkout and set permissions to `600`:

```bash
mkdir -p ~/.config/swe-bench-science
cp profiles/codex.env.example ~/.config/swe-bench-science/codex.env
cp profiles/claude.env.example ~/.config/swe-bench-science/claude.env
cp profiles/mini-swe-agent.env.example ~/.config/swe-bench-science/mini-swe-agent.env
chmod 600 ~/.config/swe-bench-science/*.env
```

For Codex, set `MODEL`, `OPENAI_API_KEY`, `CODEX_BASE_URL`,
`CODEX_WIRE_API=responses|chat`, `CODEX_VERSION`, and
`CODEX_REASONING_EFFORT`. `CODEX_WIRE_API=responses` selects the OpenAI
Responses API; `chat` selects Chat Completions. For Claude Code, set
`ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL`, and optional
`ANTHROPIC_CUSTOM_HEADERS`. mini-swe-agent uses the provider variables expected
by its selected model adapter, commonly `OPENAI_API_KEY` and
`OPENAI_BASE_URL`.

The credential file is read by Pier at runtime. It is not written to task
metadata, Dockerfiles, image layers, or result summaries. For Codex profiles
using `CODEX_BASE_URL` or `CODEX_WIRE_API`, use `tools/run_batch.py`: it
translates those fields into the Codex `config_toml` required by the gateway.

## Results

Pier writes one aggregate result and one trial directory per task/attempt:

```text
jobs/<job-name>/result.json
jobs/<job-name>/<task>__<trial>/verifier/reward.json
jobs/<job-name>/<task>__<trial>/verifier/ctrf.json
jobs/<job-name>/<task>__<trial>/verifier/test-stdout.txt
```

The wrapper additionally writes `jobs/summary.json` and `jobs/summary.csv`. For
direct Pier runs, generate them with:

```bash
python3 tools/summarize_results.py --jobs-dir jobs
```

Use `pier view jobs` to inspect trajectories. Check `result.json`,
`reward.json`, and `test-stdout.txt` together when an agent times out or a
candidate fails.

## Reproducibility And Licensing

`selection.json` records the exact task ids. Each row in `data/tasks.csv` records
the upstream repository, base commit, implementation language, source license,
material licenses and provenance, environment digest, and verifier digest. The
project tools and metadata follow the release repository's MIT terms; task
source and fixtures retain their upstream licenses. Dataset-level notices are
in [`NOTICE.md`](NOTICE.md), and affected thin task bundles also include
`fixtures/PROVENANCE.md`.

The dataset is independent of GitHub at runtime. After this snapshot is
downloaded, task materialization and evaluation use the local bundle plus Docker
Hub image digests; no task definition is fetched from the authoring repository.
