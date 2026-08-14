# Repair a batched parametric tracking workflow

A small tracking model uses reusable array-shaped data to represent a sequence
of linear dynamics terms. The supplied source can construct the model, but the
public smoke test does not complete on the untouched source.

Study the supplied paper and docs, reproduce the failure, and repair the
implementation so the same valid tracking workflow compiles and solves
consistently for the public fixture and related supported cases. Keep the fix
general: do not flatten the model into a different scientific formulation,
hard-code the fixture, or replace the solved trajectory with canned outputs.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`; do not modify the
task statement, reproduction, fixtures, workflow, or evaluation infrastructure.

Run the public smoke test with:

```bash
python reproduce.py
```

The command returns `1` when the untouched source reproduces the failure, `0`
after a successful repair, and `2` for a runner or environment failure.
