# Repair an inconsistent multiframe MR reconstruction

A medical-imaging group is replaying an archived quality-control acquisition
supplied with this task. The DICOM object is valid, all pixel frames decode, and
the historical source snapshot returns finite data with the expected
dimensionality. However, the reconstructed scientific image does not agree with
the independently archived result.

Run the offline reproduction, inspect the complete acquisition and historical
source, and repair the implementation so the complete reconstructed image
agrees with the required acquisition semantics. The repair must generalize to other
valid multiframe inputs supported by the project.

Do not hard-code this acquisition, the archived record, a filename-specific
result, or report fields. Do not modify the supplied DICOM object, archived
record, public reproduction, or generated reports.
