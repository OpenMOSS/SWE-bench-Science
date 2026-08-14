Inspect the accompanying scientific material and the supplied source snapshot, then repair the implementation so that Chemprop's reaction workflow behaves consistently on the provided organic-reaction examples.

A researcher is using the project on small organic reactions. The public workflow completes and writes finite observations, but the behavior is inconsistent with the accompanying material. The repair must generalize beyond the public examples and must not hard-code a molecule, reaction string, case-specific constant, or fixed output.

Run the public workflow with:

```bash
python reproduce.py
```

The command writes `outputs/public_report.json`. Infrastructure failures should be treated separately from scientific observations.
