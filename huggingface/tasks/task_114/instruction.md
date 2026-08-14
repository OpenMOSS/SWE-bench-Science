# Repair an implausible storage history at a planning-epoch boundary

An energy-system planning study uses the supplied historical PyPSA snapshot to
model one ordered storage experiment. The study's offline workbench completes,
but it reports an implausible availability transition around a labelled
chronology boundary. This creates an ambiguity in how much energy is actually
available for later demand.

Use the supplied reproduction, scientific reference material, and project
source to investigate and repair the implementation. The resulting behavior
must be consistent with the documented storage models and must generalize to
valid storage configurations beyond the supplied experiment.

With both per-period cyclic and initial-state conditions, cyclic governs the boundary; the initial state is not its predecessor.

Run `python reproduce.py` from this task directory to inspect the experiment.
Do not hard-code the supplied fixture, report values, labels, dimensions, or
filenames. Do not modify the fixture, workflow, reproduction command, or
generated-report contract.
