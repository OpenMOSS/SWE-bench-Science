Establish boundary-regime operator and energy closure in the TERPSICHORE-native path

You are given a reduced source snapshot from a TERPSICHORE-style ideal MHD
stability workflow.

The current implementation already supports a simpler baseline stability path,
but the included fixed-boundary reproduction exposes an incomplete capability:
once the problem definition moves from free boundary into progressively more
constrained fixed-boundary settings, the reduced implementation no longer
carries that meaning coherently through coefficient construction,
potential/kinetic operator assembly, and interval/scalar energy diagnostics.

Inspect the source and run:

    python reproduce.py

The reproduction writes the observed boundary profiles, interval quantities,
and adjacent-regime contrasts under `outputs/`. The command returns nonzero
if those observations are empty, incomplete, or non-finite; it does not apply
verifier-only boundary-regime thresholds.

Your task is to complete the implementation so that a ladder of boundary
regimes is handled consistently through the full reduced capability chain.

The intended capability chain is:

    boundary problem definition -> interval-wise boundary response -> coefficient tensors -> potential/kinetic operator blocks -> interval energy -> scalar interpretation

Do not hard-code:

- the included boundary ladder;
- a single list of expected numbers;
- only the final growth-rate-like scalar;
- only one matrix block while leaving the interval-energy path inconsistent.

Do not bypass the coefficient/operator path by writing directly into the final
report. The implementation should support the general boundary-regime workflow
represented by the supplied task.

Internet access is not available during evaluation.
