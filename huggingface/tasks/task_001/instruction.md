# Repair an inconsistent transition-state rotor workflow

A reaction-chemistry workflow is using the supplied historical source to
prepare transition-state graph data for a high-energy reaction campaign. The
inputs are valid graph representations and the workflow reaches the graph
analysis stage, but equivalent presentations of one transition state do not
give a consistent rotor observation.

Run the offline reproduction, read the supplied scientific method material, and
inspect the complete source snapshot. Repair the implementation so that the
documented transition-state rotor behavior is representation-invariant for all
supported valid molecular graphs and reaction-edge arrangements. Do not
hard-code the supplied graph, atom keys, a fixed output, or the public report.

Work only under this task directory.  The evaluation environment is offline;
all required source files and dependencies are provided.  Do not modify the
scientific fixtures, the public reproduction, or generated reports.
