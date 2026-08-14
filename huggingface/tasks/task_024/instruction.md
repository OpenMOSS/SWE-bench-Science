# Restore coherent inference in a centered factorial-effects model

A collaborative assay-calibration workflow uses the supplied PyMC source
snapshot to analyze measurements from several laboratories and protocols. The
Gaussian model contains centered laboratory effects, centered protocol effects,
and a centered laboratory-by-protocol interaction. The public workflow exposes
posterior observations and the declared identifying constraints; the verifier
checks the distribution semantics across additional shapes, scales, and
support configurations.

Run `python reproduce.py` to reproduce the scientific discrepancy. Read the
supplied method material, inspect the complete source snapshot, and repair the
implementation so that the posterior calculation represents the documented
model for all supported inputs. Preserve the public distribution API and the
meaning of its scale and support. The repair must generalize beyond the public
laboratories, protocols, data matrix, prior scales, sampling seed, and reported
contrasts.

Do not modify `reproduce.py`, `reproduction.md`, the fixture, task metadata,
or the evaluation harness. Generated files belong under `outputs/`.
