# Repair a valid OpenMC fixed-source workflow

You are repairing a historical source snapshot of OpenMC, a Monte Carlo
particle-transport code used in reactor, shielding, detector, and other
radiation-transport studies.

A research workflow exports the supplied fixed-source model successfully, but
the transport calculation terminates without producing a usable scientific
result. A separate minimal calculation in the same environment completes, so
the reported behavior is not explained by a missing compiler, an unavailable
Python package, or absent online nuclear data.

Reproduce the observation, inspect the complete source snapshot, and use the
bundled paper and official documentation to determine why this valid model is
not handled correctly. Repair the underlying implementation while preserving
the documented OpenMC input model, public Python API, and behavior of other
supported calculations. The repair must describe and implement a general
scientific/numerical rule; it must not special-case the supplied files or their
literal values.

Run the public observation with:

```bash
python reproduce.py
```

The public command is a smoke test, not a complete oracle. Generated files are
written below `outputs/`. Do not edit the fixtures, the reproduction program,
or generated reports to claim success. Changes should be made in `source/` and
must remain buildable and runnable without network access.
