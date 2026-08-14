# Task

The source tree contains a pre-fix snapshot of xarray-spatial. A small
georeferenced surface and several clipped target views are included as an
offline workbench for the normal raster reprojection workflow.

Run the public reproduction, study the supplied project material and source,
and repair the implementation so valid raster remapping respects the coordinate
geometry, nodata convention, and requested sampling method for supported input
grids. The repair must generalize to rasters and target views beyond the
included case.

Work only in this task directory. You may modify files under `source/`. Do not
special-case the included raster, view names, report fields, or fixture values.

Use:

```bash
python reproduce.py
```

The report is a finite workflow observation. Evaluation uses additional
behavioral checks.
