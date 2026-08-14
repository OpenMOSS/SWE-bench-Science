# Average referencing gives inconsistent results across application routes for mixed-modality recordings

I am preprocessing mixed-modality intracranial recordings with the
supplied MNE-Python source snapshot. My recordings contain channels of
several types (for example sEEG depth contacts and ECoG grid contacts in
the same file), and I re-reference them with an average reference over
the channel types I care about, using `set_eeg_reference`.

The library offers two routes for this — direct application and the
projection route — and both are required to implement the same
operation. For valid inputs both routes complete without errors, but the
referenced results are not consistent with the average-reference
expected average-reference semantics, and the two routes do not agree with
each other on mixed-type recordings. On single-modality recordings
everything behaves as documented.

Run `python reproduce.py` from the task directory. It builds the
synthetic recordings in `fixtures/recording_manifest.json`, applies the
average reference through both routes, and reports the post-referencing
subset means and the deviation between the routes.

Inspect the source snapshot and the public reproduction, and repair the implementation so that average referencing
behaves according to the documented semantics for all valid inputs: any
combination of supported channel types, any channel counts, and both
application routes. The repair
must not change behaviour that already conforms to the expected semantics
(single-modality referencing, explicit channel-list references, excluded
channel types), and must not hard-code the public fixtures, channel
names, or channel-type combinations.

Keep the changes limited to the scientific implementation. Do not use the
network or add external data files.
