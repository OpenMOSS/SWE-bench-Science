Extend the current TERPSICHORE-native external-region implementation so it can
correctly support the `projection_wall` geometry mode, not just the simpler wall
construction already present in the reduced source snapshot.

Inspect the source snapshot and run the public reproduction, then complete the
implementation so projection-wall geometry changes propagate through the
pseudo-vacuum construction and into downstream external-region scientific
payloads.

Use the supported `projection_wall` configuration and observed behavior to
trace the representation through the external-region implementation.

For this task, `projection_wall` should be treated as a wall-construction
regime rather than a cosmetic parameter tweak. The constructed outer geometry
must remain compatible with the existing downstream external-region machinery;
it should not introduce a disconnected one-off path that only satisfies a
single reproduction case.

Constraints:

- keep the solution generic and array-based;
- do not hard-code the public reproduction values;
- preserve the simpler wall mode already supported by the snapshot;
- keep the public reproduction runnable without internet access.
