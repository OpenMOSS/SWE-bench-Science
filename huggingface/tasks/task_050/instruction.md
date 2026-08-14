# Repair an inconsistent tensor-network state calculation

A quantum many-body group is replaying a tensor-network calculation with the
supplied historical source snapshot. The workflow finishes and produces finite
results, but the reported state quantity is not reproducible across
mathematically equivalent executions of the same calculation.

Run the offline reproduction, read the accompanying primary material, inspect
the complete source snapshot, and repair the implementation so that the
scientific calculation is consistent for valid tensor networks. The repair
must generalize beyond the supplied workload and preserve ordinary public APIs
and unrelated tensor-network behavior.

Do not hard-code the supplied input, output, or reproduction status. Do not
edit the scientific input. The public reproduction is only a smoke test; use
the references and source to establish the general invariant and validate the
repair on additional valid calculations.
