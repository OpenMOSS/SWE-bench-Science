# Repair inconsistent energies across equivalent periodic representations

A materials-simulation group is validating an archived diamond calculation
with two established periodic electronic-structure workflows.  One workflow
uses a primitive cell with a commensurate set of crystal momenta; the other uses
the corresponding enlarged real-space cell at the zone center.  Both
calculations converge normally, but their total energies per primitive cell are
incompatible at the stated numerical resolution.

Run the offline reproduction, inspect the complete scientific input and source,
and repair the historical PySCF implementation
so that equivalent periodic representations preserve the same physical
calculation.  The repair must remain valid for other cells, reciprocal cutoffs,
sampling grids, and supported periodic density-fitting routes.  Do not hard-code
the supplied crystal, its energies, or a filename-specific result, and do not
modify the supplied scientific input or generated reports.
