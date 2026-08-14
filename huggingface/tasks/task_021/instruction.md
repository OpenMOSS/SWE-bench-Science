# Complete a Missing Atomic-Liquid Thermodynamic-Integration Capability

The supplied source is a snapshot of a real research workflow for atomic-liquid
Hamiltonian thermodynamic integration. It generates simulation inputs for a
coupling path between a reference interaction and a target atomistic model.

Some scientifically valid workloads are not represented consistently by the
current implementation. The discrepancy is easy to miss in an ordinary
interior case, but becomes visible when the coupling path reaches its boundary
or when the system contains more than one chemical element with non-identical
interaction parameters.

Use the source snapshot and public generated-input artifacts to investigate the
scientific inconsistency and complete the missing
workflow capability. Preserve the existing public APIs and behavior outside the
affected scientific cases. The implementation must generalize across supported
element counts and parameter representations; do not hard-code the public
fixtures or their numeric values.

The public reproduction is generation-only and offline. It does not require a
LAMMPS executable, a machine-learning model, a scheduler, network access, or
external files. The benchmark evaluates the scientific behavior of the generated
workflow rather than a particular textual patch.
