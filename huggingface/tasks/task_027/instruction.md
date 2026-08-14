# Restore consistent NMR peak-set encoding under batch padding

You are repairing a scientific machine-learning workflow in the supplied
NMRTrans source snapshot. The workflow encodes 1H and 13C NMR peak sets into
continuous representations that a decoder consumes for molecular structure
elucidation. The required representation treats spectra as unordered peak sets
and uses permutation-equivariant attention blocks followed by
permutation-invariant pooling.

Different compounds produce different numbers of observed peaks, so spectra
are batched by appending dummy padding rows up to a common length and
recording which rows are real observations. A user running this encoding
workflow reports that the encoded spectrum is not stable under this batching:

- Encoding the same spectrum with a different number of appended padding
  rows changes the produced representations, even though the observed peaks
  are identical.
- In a padded batch, the pooled spectrum-level representation barely
  responds when a real observed peak is moved to a different chemical shift.

Both observations contradict the required set-encoding contract: the encoded
representation must be a function of the observed peaks alone, and
it must respond to chemically meaningful changes in those peaks.

Inspect the complete source snapshot and run `python reproduce.py`. Repair the implementation so that the peak-set
encoders satisfy the documented contract for all valid inputs. The repair
must generalize to arbitrary spectra, peak counts, padding lengths, random
initializations, and encoder configurations; do not hard-code the public
fixtures, specific tensor values, or a particular padding length.

Keep the overall architecture (the stacked ISAB encoder, the PMA pooling,
the learnable tokens, and the projection layers) and the existing function
signatures intact, and preserve the documented input feature layout for both
modalities. The public reproduction is only a small smoke diagnostic; use the
source call graph to determine the complete behavior that needs to be repaired. Do not use the network or add external data files.
Keep changes limited to the scientific implementation and any focused
comments that are necessary for a general fix.
