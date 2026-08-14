# Repair Split-Read Exon-Overlap Filtering

You are working with a pinned BEDTools source snapshot used in an RNA-seq
quality-control workflow.

The workflow asks which aligned reads have enough support inside annotated
exons. A junction-spanning alignment is visible when the analysis accepts any
exonic contact, but it disappears when the documented fractional-overlap filter
is enabled. A comparable contiguous alignment remains present. This changes the
count of biologically valid spliced reads even though the input records are
well-formed and sorted consistently.

Inspect the source's format handling, public fixtures, and reproduction. Repair
the implementation so discontinuous genomic records are
handled consistently with the documented interval semantics. Preserve ordinary
non-split intersection behavior and unrelated command-line behavior.

Your repair must be general. Do not hard-code the public coordinates, record
names, chromosome, threshold, block count, option order, or output mode.

Run the public reproduction with:

```bash
python reproduce.py
```

The verifier will build the repaired source and exercise additional genomic
layouts and intersection modes in a fresh offline workspace.
