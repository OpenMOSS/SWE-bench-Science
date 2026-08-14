# Restore consistent magnetic-dipole electromagnetic predictions

A geophysical electromagnetic forward-modeling workflow uses a magnetic dipole
source and reports magnetic observations at several receiver locations. The
calculation completes with finite values, but the result is not consistent with
the expected physical definition. This is especially
concerning for a forward model, because a finite numerical result can still
represent the wrong physical experiment.

Study the complete source snapshot and public reproduction. Trace the physical
calculation through the public
survey, source, simulation, and receiver interfaces, and repair the source so
that valid magnetic-dipole calculations agree with the scientific definition.
The repair must generalize to other dipole orientations, magnetic
permeabilities, receiver locations, mesh sizes, and supported forward-modeling
workflows.

Do not hard-code the supplied observations or replace the solver with a fixed
answer. Work only under this task directory. The evaluation environment is
offline; all required Python dependencies and source files are provided.

Run the public diagnostic with:

```bash
python reproduce.py
```

The command returns `0` when the candidate workflow produces finite receiver
observations, `1` only when it cannot produce a finite nonempty observation, and
`2` for an import, path, dependency, or other runner failure. The public report
is diagnostic; the verifier performs the independent physical consistency
checks on broader cases.
