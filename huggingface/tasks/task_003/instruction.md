# Repair extxyz tensor-label preservation for atomistic ML data

You are working on a pinned snapshot of `deepmodeling/dpdata`, a data conversion
library used in atomistic simulation and machine-learning potential workflows.

A collaborator is converting extended XYZ datasets produced by ASE/QUIP-style
tools into dpdata/DeepMD-style labeled systems. Energies, cells, coordinates,
and forces survive the conversion, but an important cell-level tensor label used
for stress/virial training is missing or not preserved for common extxyz files.
This is dangerous because downstream training can silently proceed with an
incomplete label set.

Inspect the source tree and repair the implementation so that
extxyz datasets following common ASE-style conventions preserve the physically
equivalent tensor information needed by dpdata. Your fix should be general; do
not hard-code the public fixture, molecule, cell size, or numeric output.
Consider the public extxyz read and write paths that users naturally exercise
through dpdata's format APIs, not only the single public reproduction script.

You can run the public reproduction workflow:

```bash
python reproduce.py
```

Keep generated files out of your patch. Do not modify task metadata. Existing
QUIP/GAP extxyz files that already provide virial-like labels should continue to
work.
