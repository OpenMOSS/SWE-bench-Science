# Repair molecular-string translation for catalogue workflows

A molecular-screening workflow uses the supplied source package to translate
SMILES strings into SELFIES and decode them back to concrete SMILES strings for
later processing. Several chemically varied catalogue entries complete this
workflow, but one library scaffold cannot be processed even though it follows
the documented surface API.

Study the supplied paper notes, reproduce the failure, inspect the source, and
repair the implementation so that valid project molecules can pass through the
SMILES-to-SELFIES-to-SMILES workflow without losing their molecular meaning.
The repair must generalize beyond the supplied fixture. Do not return fixed
molecular strings, special-case the public inputs, loosen all scientific
constraints indiscriminately, or change the public reproduction to hide a
failure.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`; do not modify the
task statement, fixtures, reproduction script, or evaluation infrastructure.

Run the public smoke test with:

```bash
python reproduce.py
```

The command returns `1` when the untouched source reproduces the molecular
translation failure, `0` after a successful repair, and `2` for a runner or
environment failure.
