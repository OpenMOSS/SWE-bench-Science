# SWE-bench Science

SWE-bench Science is a benchmark of software-engineering tasks from scientific
computing repositories. The release contains 119 tasks: 100 unrestricted-license
tasks in the default selection and 19 restricted-license tasks enabled only by
the explicit `--allow-restricted-licenses` gate. The restricted set contains
18 GPL/LGPL/AGPL-family tasks plus one academic non-commercial task.

This repository is the release control plane for
[OpenMOSS/SWE-bench-Science](https://github.com/OpenMOSS/SWE-bench-Science).
The downloadable dataset is
[OpenMOSS-Team/SWE-bench-Science](https://huggingface.co/datasets/OpenMOSS-Team/SWE-bench-Science),
and task runtime images are stored in Docker Hub under `kevinxulearning`.

## Release Layout

```text
Hugging Face dataset
  task table, statistics, task.toml, instructions, selections
          |
          | image digests
          v
Docker Hub
  119 environment images + 119 separate verifier images
          |
          v
Pier
  selected agent harness + model/provider configuration + trials
```

Each task environment image contains the baseline source, public fixtures, and
build dependencies. Each verifier image is separate, starts from the exact
environment digest, and contains private tests and the grader. Codex, Claude
Code, mini-swe-agent, and other Pier agents are selected at evaluation time;
they are not published once per task.

The standard benchmark entry point is `pier run -p ...`. This repository also
ships `tools/run_batch.py` as a convenience wrapper. It adds explicit task
selection, license gating, immutable-image pre-pulls, gateway profile
translation, and a flat result summary without changing Pier's task or verifier
semantics.

## Prerequisites

- Docker Desktop or Docker Engine with `linux/amd64` support. Apple Silicon
  machines use Docker Desktop's amd64 emulation for these images.
- Python 3.11 or newer.
- `uv` (or an equivalent Python environment manager).
- Access to the Hugging Face dataset and Docker Hub images.
- An API credential for the selected agent/provider when running a real agent.

Install the runner:

```bash
uv tool install "datacurve-pier==0.3.0"
# Without uv:
# python3 -m pip install datacurve-pier
```

## Download From Zero

```bash
mkdir swe-bench-science && cd swe-bench-science
python3 -m pip install "huggingface_hub[cli]"
hf auth login
hf download OpenMOSS-Team/SWE-bench-Science \
  --repo-type dataset --local-dir .
```

Docker Hub authentication is recommended for reliable pulls and may be required
by Docker Hub rate limits:

```bash
docker login
```

## Select Tasks

The materializer always writes an explicit `selection.json`, so the selected
task set is reproducible and does not depend on runner sampling behavior.

```bash
# Default: all 100 unrestricted-license tasks.
python3 tools/materialize.py --output tasks-selected --force

# One task, a comma-separated list, or inclusive ranges.
python3 tools/materialize.py \
  --task-id 002,005-007 \
  --output tasks-selected-small --force

# Restricted-license tasks require an explicit gate. This includes GPL-family
# tasks and task 019, whose upstream license is academic non-commercial.
python3 tools/materialize.py \
  --allow-restricted-licenses \
  --output tasks-selected-all --force
```

The 18 GPL-family ids are `003, 020, 021, 023, 032, 057, 066, 074, 075, 082,
083, 084, 085, 096, 097, 098, 100, 118`. Task `019` uses an academic
non-commercial license. All 19 ids require `--allow-restricted-licenses`.
This gate is a distribution-selection option; it does not change scoring and
does not replace the upstream license obligations.

## Run With Pier Directly

For a no-op verifier/infrastructure smoke test:

```bash
pier run -p tasks-selected-small \
  --agent nop --env docker \
  --n-concurrent 1 --n-attempts 1 \
  --no-force-build --no-delete --yes
```

For a real agent, choose one supported harness and its model/provider:

```bash
# Claude Code
pier run -p tasks-selected-small \
  --agent claude-code --env docker --env-file ~/.config/swe-bench-science/claude.env \
  --model anthropic/claude-opus-4-7 --n-concurrent 1

# mini-swe-agent
pier run -p tasks-selected-small \
  --agent mini-swe-agent --env docker \
  --env-file ~/.config/swe-bench-science/mini-swe-agent.env \
  --model openai/gpt-5 --n-concurrent 1
```

The agent name and model name are independent. `--agent` selects the harness;
`--model` selects the model/provider route. `--env-file` is loaded by Pier and
is never copied into a task image. For Codex profiles using `CODEX_BASE_URL` or
`CODEX_WIRE_API`, use the wrapper below: it translates those fields into the
Codex `config_toml` required by the gateway.

## Use The Convenience Runner

`tools/run_batch.py` pre-pulls every environment/verifier digest with
`linux/amd64`, then invokes Pier with the same task directory:

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
default task timeout). This limits only the agent stage; verifier timeouts are
separate and can be much longer for scientific builds.

### Gateway Profiles

Copy an example outside the checkout and edit only that copy:

```bash
mkdir -p ~/.config/swe-bench-science
cp profiles/codex.env.example ~/.config/swe-bench-science/codex.env
cp profiles/claude.env.example ~/.config/swe-bench-science/claude.env
cp profiles/mini-swe-agent.env.example ~/.config/swe-bench-science/mini-swe-agent.env
chmod 600 ~/.config/swe-bench-science/*.env
```

Codex profiles use `MODEL`, `OPENAI_API_KEY`, `CODEX_BASE_URL`,
`CODEX_WIRE_API=responses|chat`, `CODEX_VERSION`, and
`CODEX_REASONING_EFFORT`. Claude Code profiles use
`ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL`, and optional
`ANTHROPIC_CUSTOM_HEADERS`. mini-swe-agent uses the provider variables expected
by its selected model adapter, commonly `OPENAI_API_KEY` and
`OPENAI_BASE_URL`.

For an OpenAI-compatible gateway, `CODEX_WIRE_API=responses` selects the
Responses API and `CODEX_WIRE_API=chat` selects the Chat Completions API. Claude
Code uses the Anthropic protocol variables instead; it is not configured by
the Codex wire setting.

## Results

With the commands above, the result locations are deterministic:

```text
jobs/<job-name>/result.json                         Pier aggregate
jobs/<job-name>/<task>__<trial>/verifier/reward.json  per-trial score
jobs/<job-name>/<task>__<trial>/verifier/ctrf.json    machine-readable tests
jobs/<job-name>/<task>__<trial>/verifier/test-stdout.txt
jobs/summary.json                                   flat JSON summary
jobs/summary.csv                                    spreadsheet-friendly summary
```

`tools/run_batch.py` writes `summary.json` and `summary.csv` after Pier exits.
For a job launched directly with Pier, generate the same files with:

```bash
python3 tools/summarize_results.py --jobs-dir jobs
```

Use `pier view jobs` for the interactive trajectory view. A timeout or a
candidate failure can still have a complete verifier record; inspect
`result.json`, `reward.json`, and `test-stdout.txt` together.

## Image and License Boundaries

All 238 published task images are immutable Docker Hub `linux/amd64` digests:
119 environment images and 119 verifier images. The agent bundle does not
contain private tests or reference-answer patches. The verifier applies the
collected `model.patch` to a clean baseline and recompiles native source when
the task requires it.

The repository's own tools and documentation use the root MIT license. Task
source and fixtures retain the upstream license recorded in
`huggingface/data/tasks.csv` and `NOTICE.md`; restricted-license tasks are
explicitly gated as described above.

More detail is available in [docs/architecture.md](docs/architecture.md),
[docs/dataset-contract.md](docs/dataset-contract.md), and the
[Hugging Face dataset card](huggingface/README.md).
