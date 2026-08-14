You are working with a pinned snapshot of Osprey/FID-A, a magnetic resonance
spectroscopy processing pipeline. A collaborator is processing edited MRS data
with multiple subspectra. In a reduced synthetic reproduction, one acquisition
condition has a 180 degree polarity relationship to the others, and the current
pipeline produces an inconsistent aligned/combined result.

Run `python reproduce.py` and repair the source under
`source/` so that edited subspectra are handled consistently before alignment
and combination. The repair should be general across edited MRS datasets and
ordinary load/process workflows.

The symptom may come from inconsistent semantics between data loading and later
processing, not only from the final alignment routine.

Do not hard-code the public fixture, a particular sample count, a particular
ppm grid, a particular subspectrum count, or fixed expected numbers from the
public reproduction. Existing behavior for workflows that intentionally preserve
the original acquisition polarity should remain distinct from workflows that
need polarity-consistent spectra for alignment.
