# Repair an inconsistent peptide energy after topology import

A molecular-simulation group is reproducing an archived calculation for the
58-atom Ala-Pro-Gly-Arg peptide supplied with this task.  The coordinates and
force-field model were evaluated through several established molecular
simulation routes, and the archived total potential energies agree at their
reported precision.  Importing the supplied GROMACS files with this historical
OpenMM source snapshot completes normally, but the resulting total potential
energy is incompatible with that independent observation.

Run the offline reproduction, inspect the complete scientific input and source,
and repair the implementation so the imported model
preserves the intended physical calculation.  The repair must remain correct
for other valid GROMACS representations supported by the project.  Do not
hard-code this peptide, the archived energy, or a filename-specific result, and
do not modify the supplied scientific inputs or generated reports.
