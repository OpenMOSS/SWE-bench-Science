# Batch Evaluation Reference

`tools/run_batch.py` is the convenience wrapper for running a materialized task
selection with Pier. It does not build task images. It reads the immutable
environment and verifier references from each `task.toml`, pulls those images
for `linux/amd64`, writes a redacted run record, and invokes Pier with
`--no-force-build --no-delete --yes`.

## Prerequisites

From a downloaded release directory:

~~~bash
uv tool install "datacurve-pier==0.3.0"
docker login
python3 tools/materialize.py \
  --task-id 002,005-007 \
  --output tasks-selected-small --force
~~~

The `--path` passed to `run_batch.py` must be a materialized directory containing
`task_NNN/task.toml` directories. The runner never selects tasks implicitly and
never reads task definitions from GitHub at runtime.

## Provider Profiles

Use an env file outside the checkout. The parser accepts `KEY=value`, optional
`export KEY=value`, comments, and quoted values. It never prints credential
values or writes them to `batch-run.json`.

### Codex and OpenAI-compatible gateways

`run_batch.py` translates the following fields into Pier's Codex provider
configuration when `--agent codex` is used:

| Variable | Required | Meaning |
| --- | --- | --- |
| `MODEL` | No | Exact model route sent to the gateway; default `gpt-5` |
| `OPENAI_API_KEY` | Yes for a real run | Gateway credential |
| `CODEX_BASE_URL` | No | OpenAI-compatible gateway URL; defaults to `https://api.openai.com/v1` |
| `CODEX_WIRE_API` | No | `responses` or `chat`; defaults to `responses` |
| `CODEX_VERSION` | No | Codex runtime version passed to Pier |
| `CODEX_REASONING_EFFORT` | No | Reasoning effort passed to the Codex adapter |

Example:

~~~dotenv
MODEL=gpt-5
OPENAI_API_KEY=replace-with-your-key
CODEX_BASE_URL=https://gateway.example.edu/v1
CODEX_WIRE_API=responses
CODEX_VERSION=latest
CODEX_REASONING_EFFORT=high
~~~

`CODEX_BASE_URL` selects the model gateway. It is different from a network
proxy. A network proxy is configured with standard `HTTP_PROXY`, `HTTPS_PROXY`,
and `NO_PROXY` variables. For Docker Desktop, a proxy running on the host is
usually reached from a container as `host.docker.internal`, not `127.0.0.1`.

### Claude Code and mini-swe-agent

These harnesses receive their provider variables through Pier's `--env-file`:

~~~dotenv
# Claude Code
ANTHROPIC_AUTH_TOKEN=replace-with-your-gateway-key
ANTHROPIC_BASE_URL=https://api.anthropic.com
ANTHROPIC_CUSTOM_HEADERS=
~~~

~~~dotenv
# mini-swe-agent with an OpenAI-compatible provider
OPENAI_API_KEY=replace-with-your-gateway-key
OPENAI_BASE_URL=https://gateway.example.edu/v1
~~~

The model route is selected with the repeatable `--model` option. Provider
variables not listed here can be added to the env file and are passed through to
the selected harness by Pier.

## Basic Commands

Run a no-model infrastructure smoke:

~~~bash
python3 tools/run_batch.py \
  --path tasks-selected-small \
  --agent nop \
  --n-concurrent 1 \
  --n-attempts 1 \
  --jobs-dir jobs \
  --job-name smoke
~~~

Run Codex through a gateway:

~~~bash
python3 tools/run_batch.py \
  --path tasks-selected-small \
  --agent codex \
  --env-file ~/.config/swe-bench-science/codex.env \
  --n-concurrent 2 \
  --n-attempts 1 \
  --max-retries 1 \
  --jobs-dir jobs \
  --job-name codex-small
~~~

Run Claude Code or mini-swe-agent:

~~~bash
python3 tools/run_batch.py \
  --path tasks-selected-small \
  --agent claude-code \
  --env-file ~/.config/swe-bench-science/claude.env \
  --model anthropic/claude-opus-4-7 \
  --n-concurrent 1 \
  --jobs-dir jobs \
  --job-name claude-small
~~~

For an approximately 120-second agent-stage smoke, add
`--agent-timeout-multiplier 0.0223`. This does not shorten the verifier timeout
or any native build timeout.

## Option Reference

| Option | Default | Description |
| --- | --- | --- |
| `--path` | required | Materialized task directory |
| `--agent` | `nop` | Pier harness, such as `codex`, `claude-code`, `mini-swe-agent`, or `nop` |
| `--env` | `docker` | Pier environment backend |
| `--env-file` | unset | Provider/harness env file |
| `--model` | unset | Model route; repeat for multiple Pier model arguments |
| `--agent-env KEY=VALUE` | repeatable | Extra environment value passed to the harness |
| `--agent-kwarg KEY=VALUE` | repeatable | Extra Pier agent keyword; useful for adapter-specific settings |
| `--n-concurrent` | `1` | Number of simultaneous tasks |
| `--n-attempts` | `1` | Attempts per task |
| `--max-retries` | `0` | Pier retries after an attempt-level failure |
| `--agent-timeout-multiplier` | Pier default | Multiplier for the agent stage timeout |
| `--verifier-timeout-multiplier` | Pier default | Multiplier for verifier/build timeout |
| `--jobs-dir` | `jobs` | Directory for Pier jobs and summaries |
| `--job-name` | unset | Stable job name used in result paths |
| `--platform` | `linux/amd64` | Docker pull and derived Pier image platform |
| `--pier-bin` | `pier` | Pier executable or absolute path |
| `--skip-pull` | off | Skip Docker pulls when immutable refs are already local |
| `--no-auto-provider` | off | Do not translate `CODEX_*` profile values into Codex kwargs |
| `--no-auto-agent-adapter` | off | Use Pier's built-in Codex agent instead of the Science Bench adapter |
| `--agent-import-path` | unset | Explicit Pier agent import path |
| `--dry-run` | off | Pull/validate images and write metadata, but do not invoke Pier |

The wrapper always records the selected task IDs, selection hash, image refs,
platform, Pier version, agent/model settings, and a redacted Pier command in
`<path>/batch-run.json`.

## Results

Pier writes its job output under the selected jobs directory. The wrapper then
generates:

~~~text
jobs/<job-name>/result.json
jobs/<job-name>/summary.json
jobs/<job-name>/summary.csv
jobs/<job-name>/<task>__<trial>/verifier/reward.json
jobs/<job-name>/<task>__<trial>/verifier/ctrf.json
jobs/<job-name>/<task>__<trial>/verifier/test-stdout.txt
~~~

The summary CSV is the convenient per-task result table. Use `pier view jobs`
for trajectories and inspect `result.json`, `reward.json`, and
`test-stdout.txt` together when diagnosing a failure.

## Common Variants

Pull nothing and inspect the fully rendered command:

~~~bash
python3 tools/run_batch.py \
  --path tasks-selected-small \
  --agent codex \
  --env-file ~/.config/swe-bench-science/codex.env \
  --skip-pull \
  --dry-run
~~~

Run the 91-task science-knowledge ablation selection after materialization:

~~~bash
python3 tools/materialize.py \
  --task-id 002-082,084,086,090,097-101,111,114 \
  --allow-restricted-licenses \
  --output tasks-science-knowledge-ablation --force

python3 tools/run_batch.py \
  --path tasks-science-knowledge-ablation \
  --agent codex \
  --env-file ~/.config/swe-bench-science/codex.env \
  --n-concurrent 4 \
  --jobs-dir jobs \
  --job-name codex-science-ablation
~~~
