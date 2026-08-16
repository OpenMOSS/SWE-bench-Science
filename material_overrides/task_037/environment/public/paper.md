# Scientific and method material

This task uses the DICOM Enhanced MR model and NiBabel's historical DICOM
reader. The following standards sections are the primary method references:

- DICOM PS3.3 Image Plane Module:
  <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html>
- DICOM PS3.3 Multi-frame Functional Groups Module:
  <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.16.html>
- DICOM PS3.3 Multi-frame Dimension Module:
  <https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.17.html>
- DICOM Supplement 49, *Enhanced MR Image Storage SOP Classes*:
  <https://dicom.nema.org/medical/dicom/final/sup49_ft.pdf>

The NEMA standard pages and Supplement 49 are linked rather than copied.
Supplement 49 expressly prohibits circulation, quotation, or reproduction
without NEMA approval. A saved NiBabel documentation index remains at
`paper_assets/nibabel_dicom.html` under the NiBabel MIT license.

The public DICOM fixture is a deterministic benchmark adaptation of NiBabel's
MIT-licensed upstream `4d_multiframe_test.dcm` at commit
`5d10c5b8bb09576e24e9d316da1019fb909d7d32`. Identifiers and original pixels
were removed; the geometry was anonymized and deterministic phantom pixels
were substituted. The fixture should be interpreted using the linked standard,
the retained source documentation, and the complete acquisition metadata.
