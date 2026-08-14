# Repair an inconsistent archived elasticity workflow

A computational-materials group is replaying the complete archived silicon
campaign supplied with this task. The historical workflow parses every
calculation and produces a finite elasticity document, but a downstream
scientific audit cannot reconcile the recorded campaign and fitted response
with the stress-strain method governing the supplied workflow. Repeating the
workflow does not change the discrepancy, and no archived first-principles
calculation reports a runtime failure.

Run the offline reproduction, inspect the ordinary project output, complete
source snapshot, and task context, then repair the implementation so that
supported elasticity campaigns produce scientifically consistent records and
fitted responses. The repair must generalize to other valid crystal structures,
loading schedules, and coordinate representations supported by the project.

Do not hard-code silicon, archived numeric results, calculation identifiers, or
fixture paths. Do not replace the workflow with a fabricated document, and do
not modify the supplied scientific inputs or generated reports.
