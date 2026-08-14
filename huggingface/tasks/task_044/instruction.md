# Repair inconsistent battery-model predictions

A battery-modeling group is using this historical PyBaMM snapshot to study a
realistic lithium-ion cell parameterised for the supplied study. A
valid offline discharge workflow completes, but its scientific output does not
satisfy the discharge behavior required by the model and protocol.

Run the supplied reproduction, inspect the complete project source and task
workflow. Diagnose the cause of the inconsistent battery prediction and repair
the implementation so that the documented scientific workflow is correct for
supported inputs.

The repair must be general. Do not hard-code the supplied result, parameter
names, model class, protocol, or file paths. Do not modify the scientific
inputs, workflow, reproduction, or generated reports.
Validate your change with additional legal parameter values and model paths,
not only the public run.
