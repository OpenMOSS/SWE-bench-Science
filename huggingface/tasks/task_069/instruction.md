# Restore a complete Hi-C contact-decay analysis

A chromatin-conformation group is replaying an archived Hi-C contact map from
an experiment whose later bin-level annotations were not retained with the
interaction archive. The group needs the usual intrachromosomal
distance-dependent contact analysis as a baseline for subsequent work.

The supplied map is a valid offline archive and the included workflow is an
ordinary project workflow.  On the historical source, however, that workflow
does not produce a complete scientific report.  This is inconsistent with the
contact-map interpretation described in the supplied scientific material.

Run the reproduction, inspect the source and the reference material, and repair
the implementation so that the intended analysis is scientifically consistent
for valid inputs.  The repair must generalise: do not hard-code the supplied
archive, a chromosome name, a map resolution, a count pattern, or a fixed
numeric result.  Do not modify fixtures, the reproduction harness, generated
reports, task metadata, or task instructions.
