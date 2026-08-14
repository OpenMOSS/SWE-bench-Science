# Repair bond-order species reporting

You are working with a local snapshot of ReacNetGenerator, a tool for building
reaction networks from reactive molecular-dynamics trajectories.

Run the public workbench:

```bash
python reproduce.py
```

The bundled bond-file fixture exercises a small ring-like structure under
several bond-order assignments. Inspect the report and repair the source so the
molecule, species, and reaction outputs are chemically consistent for the
fixture.

Keep changes inside `source/`. Do not edit the public fixtures or the
reproduction script.

Do not hard-code the supplied fixture or report values. Your fix should work for
other bond-order variants that preserve atom membership and bonding
connectivity.
