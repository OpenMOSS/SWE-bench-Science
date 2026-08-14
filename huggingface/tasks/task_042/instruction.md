# Repair an inconsistent solar-coordinate archive workflow

A solar-observation catalogue uses the supplied scientific package to attach
coordinate objects to a table before archiving the catalogue for later
analysis. The coordinates describe a short sequence of features observed from
changing locations. Object construction and the in-memory analysis are valid,
but the archive/reload workflow does not yield a catalogue that can be reused
consistently in the same downstream analysis.

Reproduce the problem, inspect the source and public workflow, and repair the
implementation so that valid solar-observation
catalogues retain their scientific meaning through supported archive
workflows. The repair must generalize beyond the supplied catalogue. Do not
replace scientific objects with fixed outputs, special-case the supplied data,
or change the public reproduction to hide a failure.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`; do not modify the
task statement, reproduction, fixtures, workflow, or evaluation infrastructure.

Run the public smoke test with:

```bash
python reproduce.py
```

The command returns `1` when the untouched source reproduces the scientific
archive failure, `0` after a successful repair, and `2` for a runner or
environment failure.
