# Terrain-following atmospheric data on isentropic surfaces

A researcher is using the supplied MetPy source snapshot to interpolate a
terrain-following atmospheric model dataset onto potential-temperature
surfaces. The reduced dataset is finite and carries the model-level coordinate,
thermodynamic state fields, units, and coordinate metadata normally available
to this workflow. The calculation does not produce an isentropic dataset,
although the requested surfaces cross the supplied atmospheric columns and
ordinary pressure-level products remain usable.

Inspect the source, run the public reproduction, and repair the implementation
so that supported atmospheric datasets can be interpolated consistently with
the expected coordinate semantics. Preserve supported existing workflows and
generalize beyond the
public reduced dataset and numeric values.

Run:

```bash
python reproduce.py
```

Do not hard-code the public coordinate values, pressure profile, dimensions, or
expected output. The task must remain fully offline.
