# Restore chemically consistent proteoform ion annotations

A proteomics curation group is replaying a small offline precursor-annotation
batch supplied with this task. Every record is intended to be legal under the
included ProForma material, and the historical source can parse the batch.
However, the workflow does not yield a complete table of usable precursor
observations. The reproduction records the candidate precursor measurements it
does obtain, as well as unavailable observations. A present measurement is
evidence from the historical workflow, not by itself a correctness certificate.

Run the offline reproduction, inspect the source and the supplied scientific
material, and repair the implementation so that valid annotations are handled
consistently with the ProForma definition. The repair must generalize across
valid inputs supported by the project, not merely make the supplied records
finish.

Do not hard-code a record identifier, annotation string, output count, or fixed
numeric result. Do not modify the supplied fixtures, reproduction script, or
generated reports.
