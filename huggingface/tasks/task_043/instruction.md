# Repair an inconsistent porous-volume characterization

A porous-media research group is reprocessing segmented X-ray tomography
data from sandstone with this historical PoreSpy source snapshot.  The
supplied offline workflow completes normally, but the summaries produced from
the supplied segmented volume and an explicit axis-permuted representation of
that same volume are not mutually consistent. A radial two-point
characterization should not depend on which array axis stores a physical
direction.

Run the reproduction, inspect the supplied sample data and project source, and
repair the implementation so the
scientific characterization is consistent with the definitions supported by
the project.  The repair must generalize to other valid segmented images and
documented analysis options.

Do not hard-code the supplied volume, permutation, any public observation,
fixed dimensions, or filename-specific behavior. Do not modify the scientific
input, workflow, public observations, or generated reports.
