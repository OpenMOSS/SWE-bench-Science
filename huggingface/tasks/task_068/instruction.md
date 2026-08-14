# Restore biologically consistent retrieval from a VCF archive

A cohort-analysis workflow stores a local VCF archive and retrieves records by
genomic region.  The supplied archive slice is accepted by the command-line
workflow, but a record that should be relevant to an interior genomic location
is absent from the result.  A nearby control query still returns a record, so
the run looks superficially healthy while changing the biological interpretation
of the archive search.

Run the supplied reproduction, inspect the source snapshot, and use the local
VCF specifications to repair the implementation.  The corrected software must
give biologically consistent behavior for valid supported records, not merely
for the supplied archive slice.  Do not hard-code the example's chromosome,
coordinates, record count, or a fixed output.

