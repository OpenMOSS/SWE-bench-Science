# Repair an ill-conditioned overlap band-postprocessing workflow

A materials post-processing workflow uses the supplied scientific package to
compute band energies for a non-orthogonal tight-binding model. The input
matrices are Hermitian and represent a valid inference-time case where the
overlap basis contains nearly redundant modes. The workflow should still return
finite, reusable band data and a downstream Fermi-level estimate for the
physical states it can resolve.

Study the supplied paper notes, source snapshot, and public reproduction. Repair
the implementation so that the post-processing workflow preserves the scientific
meaning of generalized eigenvalues when the overlap basis becomes poorly
conditioned. The repair must generalize beyond the bundled matrices and must not
replace the calculation with fixed outputs, special-case the fixture, or change
the public reproduction to hide a failure.

Treat this as an explicitly requested handling mode for the supplied workflow.
Ordinary calls that do not request this treatment should keep their existing
behavior rather than silently reclassifying unresolved overlap modes as usable
band states. Any metadata used by downstream consumers to distinguish resolved
states from dense padding should correspond one-to-one with the returned band
entries.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`; do not modify the
task statement, reproduction, fixtures, workflow, or evaluation infrastructure.

Run the public smoke test with:

```bash
python reproduce.py
```

The command returns `1` when the untouched source reproduces the scientific
post-processing failure, `0` after a successful repair, and `2` for a runner or
environment failure.
