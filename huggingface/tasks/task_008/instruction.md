The current TERPSICHORE-native migration slice already covers the reduced
internal-region stability path, but it does not yet correctly establish the
first wall-coupled external-region capability needed for vacuum plus conducting
wall analysis.

Read the provided method context and source snapshot, run the public
reproduction, and complete the missing capability so the implementation no
longer behaves like an internal-only scaffold when a vacuum region and an
explicit conducting wall are part of the problem. A correct solution should let
materially different conducting walls produce distinct global potential-energy
and stability observations while the no-explicit-wall fallback remains
available.

Constraints:

- keep the solution generic and array-based;
- do not hard-code the public reproduction values;
- preserve the no-explicit-wall fallback path;
- keep the public reproduction runnable without internet access.
