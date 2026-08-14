# Inconsistent archived observables

A molecular-modelling workflow is replaying archived DFTB+ calculations with
this historical source snapshot. Several valid archived records complete
successfully, yet some reported observables do not stay consistent across the
documented input conventions.

Run the supplied offline workflow, inspect the raw reports, the complete source
snapshot, the official DFTB+ materials, and the documented input conventions.
Repair the historical implementation so supported calculations behave
consistently for valid inputs. The repair must generalize beyond the supplied
archives. Do not hard-code the fixtures or reports, and do not modify the
public workflow or scientific inputs.
