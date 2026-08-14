# Repair a physical surface-overlap calculation

You are working on a scientific image-analysis workflow built from the supplied MONAI source snapshot. The workflow compares an automated segmentation with a reference segmentation using a normalized surface-overlap score. The supplied paper explains why this kind of score is useful for contour-based evaluation in radiotherapy and why the tolerance is a physical distance.

Run the public reproduction and inspect the source and paper. The command completes on the supplied inputs, but the finite score changes too much when the same physical study is represented on two different voxel grids. This is a scientific consistency problem, not an installation or syntax problem.

Repair the implementation so that the metric has a physically meaningful interpretation for supported 2-D and 3-D binary, one-hot, batch-first inputs. Preserve the normal public API, distance choices, reduction behavior, batch handling, and well-defined empty-class behavior. Keep a compatible unit-grid or legacy behavior when the caller has not requested a physical-spacing measurement.

Do not hard-code the supplied arrays, score values, grid shapes, or tolerance. The repair must generalize to new geometries, spacing orders, thresholds, and input batches. Use the accompanying paper and the source's existing abstractions to determine the correct scientific behavior. Do not modify the public reproduction to conceal a failing result or bypass the metric implementation.

The source snapshot includes a small import-compatibility layer so that the relevant MONAI metric path runs in the offline task environment. Do not turn package initialization or unrelated optional MONAI modules into a separate task.
