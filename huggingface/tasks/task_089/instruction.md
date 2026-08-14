# Repair inconsistent ORCA excited-state spectrum parsing

A computational-chemistry workflow imports ORCA excited-state spectra from a
historical source snapshot. The parser completes and returns finite transition
data, but a downstream spectrum summary made from the parsed attributes is not
consistent with the supplied ORCA-style record.

Run the public reproduction, inspect the complete source snapshot and supplied
scientific material, and repair the implementation so valid ORCA excited-state
spectrum records retain their scientific meaning in the parsed data model. The
repair must generalize to other valid ORCA spectra, output-version layouts,
additional transition-property sections, and related spectroscopy sections that
may appear in the same output.

Do not hard-code the supplied fixture, spectrum names, line numbers, numerical
values, or generated report. Work only in this task directory. The evaluation
environment is Linux and has no network access. You may modify files under
`source/`; do not modify the public reproduction, fixtures, workflow, or
evaluation infrastructure.

Use:

```bash
python reproduce.py
```

The command is a diagnostic workflow. It returns `0` when the parser can produce
a finite nonempty spectrum observation, `1` when it cannot, and `2` for a runner
or dependency failure. The independent verifier checks scientific consistency on
broader spectra.
