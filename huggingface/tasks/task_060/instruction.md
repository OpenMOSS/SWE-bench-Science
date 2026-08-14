# Restore a complete cross-band drift-correction recording

An electrophysiology group archived the Neuropixels AP and LF streams and the
registration track supplied with this task.  The track is used with the LF
acquisition context to correct a region of the AP recording before downstream
spike analysis.  All inputs load through the historical SpikeInterface source
snapshot, but the complete corrected recording cannot be materialized into a
scientifically usable result.

Run the offline reproduction, inspect the full source, real acquisition
metadata, project manuals, and papers, and repair the implementation so this
normal workflow completes.  The repair must preserve the intended physical
registration for other valid recordings and registration tracks supported by
the project.  Do not hard-code this session, its channel region, its track, or
the public report, and do not modify the supplied scientific inputs.
