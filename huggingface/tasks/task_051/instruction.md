# Repair an inconsistent planetary gradient-tensor calculation

A planetary-science group is reprocessing an archived magnetic-field model with
this historical SHTOOLS source snapshot.  In their analysis, two complete
second-order field calculations based on equivalent representations of the same
spherical-harmonic potential produced smooth finite maps that were not
physically consistent after being expressed in a common Cartesian frame.

Run the offline Mars field study as a realistic project workflow, inspect its
raw products, the complete source, and coefficient model, and repair the
implementation so equivalent
representations of a supported potential produce the same physical tensor
field.  The repair must generalize to other supported coefficient models,
truncation degrees, grid modes, and both gravitational and magnetic tensor
workflows.  Do not hard-code the supplied model, a reported status, or a
fixture-specific result, and do not modify the scientific input or the
generated report.
