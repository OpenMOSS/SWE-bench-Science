# Repair an inconsistent alloy equilibrium assessment

A materials-thermodynamics group is replaying literature-linked alloy studies
with the supplied historical pycalphad source and databases. The calculations
complete and return finite datasets, but several observations no longer agree
with the group's archived results:

- a composition-temperature phase boundary moves when an equivalent database
  representation is admitted to the same assessment;
- the associated phase fractions and internal-state evolution cease to form a
  physically consistent transition;
- chemical-potential and heat-response curves disagree with the corresponding
  baseline calculation; and
- the equilibrium topology depends on a representation that should not create
  a new thermodynamic state for the requested components.

Run the offline workflow, inspect the databases and source snapshot, and repair
the scientific
implementation. Determine the common cause rather than treating the symptoms
independently. The repair must generalize to other valid CALPHAD database
representations and supported phase states while preserving public APIs and
unrelated model behavior.

Do not hard-code the supplied grids or generated artifacts, and do not modify
the scientific input files. The public workflow only establishes that the real
project calculation runs and saves results; correctness is evaluated on
independent scientific cases.
