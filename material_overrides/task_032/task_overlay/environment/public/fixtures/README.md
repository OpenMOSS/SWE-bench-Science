# Synthetic GROMACS fixtures

These files were written for SWE-bench Science and are distributed under the
repository MIT license. They do not contain CHARMM, AMBER, or other third-party
force-field parameter sets.

`combination_rule_1` expresses Lennard-Jones parameters as C6/C12 coefficients.
`combination_rule_3` expresses the same model as sigma/epsilon. The decimal
values follow directly from `C6 = 4 epsilon sigma^6` and
`C12 = 4 epsilon sigma^12` using benchmark-selected parameters.
