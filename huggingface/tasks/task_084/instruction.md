# Repair ABACUS relaxation archive/reload semantics

The supplied ABACUS relaxation examples can be loaded, but the supported
archive/reload workflow does not preserve the trajectory in a scientifically
usable form consistently across the provided examples.

Study the supplied paper and method notes, reproduce the issue, inspect the
source, and repair the implementation so that valid ABACUS relaxation
catalogues remain scientifically coherent through the supported
archive/reload workflow. The repair must generalize beyond the supplied
examples. Do not replace scientific objects with fixed outputs,
special-case the supplied data, or change the public reproduction to hide the
failure.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`; do not modify the
task statement, reproduction, fixtures, workflow, or evaluation
infrastructure.

Run the public smoke test with:

```bash
python reproduce.py
```

The command returns `1` when the untouched source reproduces the issue, `0`
after a successful repair, and `2` for a runner or environment failure.
