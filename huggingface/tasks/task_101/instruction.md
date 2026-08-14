# Repair an inconsistent battery-model reproduction

A battery-model workflow in the supplied package does not complete under one of
the documented model configurations exercised by the public reproduction. Run the
public reproduction, inspect the source snapshot and the background material, and
repair the implementation so the documented workflows produce finite, physically
plausible results.

The repair must generalize beyond the supplied example. Do not hard-code the
fixture, a single parameter set, or a fixed output trace.

Work only in this task directory.

Use:

```bash
python reproduce.py
```

The script reports whether the public workflow completed, whether it hit the
expected scientific failure before repair, or whether an infrastructure problem
prevented the check from running.
