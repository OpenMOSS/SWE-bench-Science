# Restore equivalent GROMACS nonbonded representations

A molecular-simulation group is validating a historical OpenMM source snapshot
with two small, benchmark-authored GROMACS models. The models encode the same
two-particle Lennard-Jones interaction using two standard combination-rule
representations. Both import successfully, but they produce incompatible
potential energies on the same coordinates.

Run the offline reproduction, inspect the complete synthetic inputs and source,
and repair the importer so equivalent supported representations preserve the
same physical model. The repair must generalize to other atom labels, parameter
values, declaration orders, explicit pair terms, and supported combination
rules. Do not hard-code the supplied files or replace computed values with
constants.
