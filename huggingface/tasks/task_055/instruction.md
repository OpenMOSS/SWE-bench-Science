# Restore a scientific template-comparison workflow

An astronomy group is comparing an archived extraction of a real SDSS DR16
observation with a lower-resolution local template through the project's
template-comparison workflow.  The command runs to completion, but the
comparison does not produce a usable result consistent with the archived
analysis.

Inspect the supplied scientific paper, the project documentation, the complete
source snapshot, and the offline reproduction.  Repair the implementation so
that the workflow behaves correctly for valid spectra and remains compatible
with the project's public APIs.

The supplied SDSS case is evidence of a real workflow failure, not the complete
specification.  Do not hard-code the dataset, wavelength values, archived
score, or a filename-specific result.  Use the scientific material and the
source's existing semantics to make a general repair.  Do not modify the
supplied scientific inputs or generated reports.
