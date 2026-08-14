# Restore consistent tapered-filament free response

A filament-mechanics workflow uses the supplied scientific package to study
slender specimens whose radius changes along their length.  Each specimen is
initially straight, free of imposed loads, and given a uniform velocity.  A
single material response setting is then used to characterize its free
response.

For tapered specimens, the recorded local response changes markedly with the
cross-section even though the material setting is common to the specimen. This
makes results from different manufactured taper profiles difficult to compare
and is not consistent with the intended material interpretation of that
setting.

Use SI units for the supplied workbench: lengths and radii are in metres,
density is in kg/m^3, velocity is in m/s, and the package's material-response
setting is an inverse-time rate in s^-1. This task's rate convention is the one
used by the rod API; the paper also discusses other viscous coefficients with
different units, which are not substituted for the workbench setting. The
supplied workbench directly exercises one translational free-response path. The
package supports other free-response dynamics and assembled multi-specimen
workflows; a repair must preserve valid public interfaces and physically
meaningful behavior outside the three displayed profiles.

Use the supplied source, paper, and reproducible workbench to repair the
implementation so that valid tapered-filament simulations retain physically
consistent free-response behavior across supported workflows. Preserve valid
public interfaces and scientific behavior outside the supplied example. Do not
hard-code the supplied profiles or output values, special-case the workbench,
or replace the simulation with fixed results. If an apparent local change does
not remain consistent when you vary valid geometry or motion, trace the model
and revise the repair rather than hiding the discrepancy.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`; do not modify the
task statement, paper material, reproduction workflow, or evaluation
infrastructure.

Run the public workbench with:

```bash
python reproduce.py
```

The command writes a diagnostic observation report. A completed public
workflow shows that the experiment ran; it is not the final correctness
decision.
