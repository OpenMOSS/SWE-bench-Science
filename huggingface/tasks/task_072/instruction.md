# Repair an incomplete DICOM color image presentation workflow

A medical-imaging research workflow is replaying a small local suite of color
objects through the historical source snapshot. The objects are local, valid
for the workbench, and their stored color samples can be decoded into finite
numeric arrays. However, the normal scientific presentation suite does not
complete with consistent color-image representations for all objects.

Run the public reproduction, inspect the source code and the supplied DICOM and
pixel-data reference material, and repair the implementation so that supported
DICOM color images are interpreted consistently by the public pixel workflow.
The repair must generalize beyond the supplied files and must not hard-code a
filename, array shape, sample value, or fixed output.

Do not modify the fixture, public reproduction script, generated reports, or
task metadata.
