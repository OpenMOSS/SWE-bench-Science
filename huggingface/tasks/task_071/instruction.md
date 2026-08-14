# Repair an orientation-sensitive fiber-scattering reduction

A grazing-incidence/fiber diffraction reduction was run on a detector-panel
acquisition whose fiber-axis orientation convention is recorded in the
experimental setup. The workflow completes, but changing that supported
acquisition setting produces a reciprocal-space observation whose movement is
inconsistent with the supplied scattering geometry for an asymmetric panel.
That makes it difficult to interpret whether observed features are in-plane or
out-of-plane.

Use the supplied offline source, scientific material, and reproduction
workbench to investigate the discrepancy and repair the implementation. The
orientation value in this task belongs to the project's Fiber/sample-axis
workflow; it is not the separate detector metadata enum. The repair must work
for the supported Fiber orientation conventions generally, not only for the
provided panel. Do not modify task metadata, fixtures, the public runner, or
the evaluation harness. Place your solution in `artifacts/model.patch`.
