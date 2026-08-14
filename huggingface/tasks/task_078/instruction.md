# Repair an inconsistent astronomical aperture workflow

An astronomical image-analysis workflow runs equivalent observation workloads
on several calibrated image grids. The calculations complete, but a normalized
scientific quantity changes when only the coordinate representation changes.

Study the supplied scientific material and source snapshot. Run the public
workload survey, inspect the implementation, and repair the underlying
representation handling so the same physical workload gives the same
normalized quantity across finite, nonsingular calibrated maps, within normal
sampling and floating-point variation. The repair must generalize beyond the
supplied survey and must not hard-code a particular grid, angle, center, scale,
workload, or fixed numeric output.

Work only under this task directory. The evaluation environment is offline; all
required Python dependencies and source material are provided.

Run the public diagnostic with:

```bash
python reproduce.py
```

The command returns `0` after producing a finite measurement survey and `2`
for an import, path, dependency, or other runner failure. The public report is
an observational workbench rather than a correctness oracle; the verifier
checks broader scientific consistency cases.
