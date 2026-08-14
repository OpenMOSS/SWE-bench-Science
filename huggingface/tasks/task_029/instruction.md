# Annotation equivalence fails after construct-orientation normalization

A construct-annotation workflow built on the supplied Biopython snapshot
normalizes circular DNA records into the opposite display orientation before
shipping GenBank files to downstream design and review tools. The input batch
is stored in `fixtures/construct_manifest.json` and contains the mixture of
feature representations used by the delivery workflow.

The normalization and export complete without exceptions, and the generated
GenBank records can be parsed again. Nevertheless, the downstream annotation
equivalence check rejects part of the batch: the nucleotide sequence and
basic file structure remain usable, but the transformed annotations do not all
describe the same biological content.

Run `python reproduce.py` from the task directory. It executes the user
workflow and reports only record-level structural observations. The public
workflow is intended to show useful delivery behavior without embedding a
second annotation oracle.

Use the supplied scientific references, complete source snapshot, input
records, and any diagnostic experiments you design yourself to determine why
the library produces inconsistent annotations. Repair the scientific
implementation for general valid records without hard-coding the public
batch or its stored outputs. Existing behavior for unaffected annotation
representations and ordinary sequence operations must remain compatible.

Do not use the network or add external data files. Keep the repair inside the
supplied source snapshot.
