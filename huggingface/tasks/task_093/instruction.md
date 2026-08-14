# Repair a patient-space round trip in MONAI

You are working on a compact medical-imaging I/O workflow built from the supplied MONAI source snapshot. A small voxel study should keep the same physical meaning when it goes from a reader-produced `MetaTensor` into an ITK image and back through the direct reader path.

Run the public reproduction and inspect the source and supporting notes. The command completes on the supplied inputs, but the round-tripped image no longer agrees with the direct reader route on the same study. This is a scientific coordinate-consistency problem, not an installation or syntax problem.

Repair the implementation so that the bridge preserves the same patient-space interpretation for supported 2-D and 3-D scalar volumes, including studies whose NRRD header omits `space` metadata. Preserve the public API, the reader metadata contract, and the round-trip behavior for equivalent explicit-space and implicit-space inputs. Do not hard-code the supplied array values, affine values, or file names. The fix must generalize to new studies, spacings, and origins.

Do not modify the public reproduction to conceal a failing result or bypass the reader, bridge, or writer implementation.
