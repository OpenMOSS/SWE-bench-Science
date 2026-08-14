# Repair a symmetric composite laminate ABD calculation

A composite-shell property workflow computes ABD matrices for laminated
plates. A symmetric laminate and the same ply stack written explicitly should
carry the same physical stiffness meaning through the supported workflow, but
the supplied package does not preserve that behavior.

Reproduce the issue, inspect the source and public workflow, and repair the
implementation so valid laminate descriptions retain their scientific meaning
across supported symmetric and explicit layup calculations. The repair must
generalize beyond the supplied case. Do not special-case the fixture, hardcode
matrices, or change the public reproduction to hide a failure.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`; do not modify
the task statement, reproduction, fixtures, or evaluation infrastructure.

Run the public smoke test with:

```bash
python reproduce.py
```

The command returns `1` when the untouched source reproduces the laminate
consistency failure, `0` after a successful repair, and `2` for a runner or
environment failure.
