# Repair inconsistent finite-volume advection edge states

An energy-materials transport workflow uses the supplied scientific package to
build one-dimensional finite-volume advection models. The models discretise a
cell-centered state, reconstruct edge states for the advective flux, and then
advance a transient source problem. The calculations finish with finite values,
but the edge-state observations and the transported profiles are not
consistent with the finite-volume semantics documented for this package.

Study the source snapshot, public documentation assets, and public
reproduction. Trace how symbolic spatial operators become edge-centered
quantities during discretisation, and repair the source so that valid
upwind/downwind advection workflows are internally consistent with the package's
finite-volume boundary representation. The repair must generalize beyond the
provided mesh, tracer profile, boundary value, velocity direction, and source
term.

Do not hard-code the supplied observations or replace the model with fixed
outputs. Work only under this task directory. You may modify files under
`source/`; do not modify the task statement, fixtures, workflow, reproduction,
or evaluation infrastructure. The evaluation environment is offline.

Run the public diagnostic with:

```bash
python reproduce.py
```

The command returns `0` when the finite-volume workflows produce finite,
nonempty scientific observations, `1` only when the workflow cannot produce
finite observations, and `2` for an import, dependency, path, or runner
failure. The public diagnostic is a workbench; the verifier performs
independent scientific consistency checks on broader cases.
