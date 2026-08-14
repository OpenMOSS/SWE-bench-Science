# Restore consistent compressed Deep Potential tabulation

A molecular-simulation group is evaluating a compressed Deep Potential
workflow using the supplied C++ source snapshot. The calculation completes and
returns finite descriptor contributions and finite sensitivity values, but a
small sweep of compressed-table observations is not consistent with the
energy-force relationship described by the supplied scientific material.

Run the public reproduction, study the supplied paper and method material, and
inspect the complete source snapshot. The public command is a diagnostic
workbench: read its finite observations rather than treating process success as
scientific correctness. Repair the implementation so that valid
compressed-model tabulation workflows preserve the same scientific meaning for
descriptor values and their sensitivities across supported descriptor families
and valid table configurations.

The repair must generalize beyond the public probe. Do not hard-code the
public coefficients, coordinates, report values, descriptor family, or generated
driver. Do not replace the scientific calculation with a fixed report or change
the task material to hide the inconsistency.

Work only under this task directory. The evaluation environment is Linux,
offline, and provides a C++ compiler. You may modify files under `source/`.

Run the public diagnostic with:

```bash
python reproduce.py
```
