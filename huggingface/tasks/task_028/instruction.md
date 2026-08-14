# Task

I am analyzing a single-cell perturbation data set with the D-SPIN framework
(using the supplied source under `source/`). I trained a model and saved
the inferred perturbation response vectors to
`fixtures/public/model_responses.npz`; the sample metadata table — which
sample is a control, and which batch each sample belongs to — is in
`fixtures/public/sample_metadata.csv`.

Following the documented analysis workflow, I then computed each sample's
response relative to the control samples: every sample's relative response
is supposed to be its response vector minus the average response of the
control samples in the same batch, and samples in a batch without control
samples use the average over all control samples.

The results do not behave the way the definition says they should:

- the control samples' own relative responses are clearly not centered at
  zero within their batch, so the baseline that was subtracted cannot be the
  batch's control average;
- when I reorder the rows of the metadata table and rerun the analysis, the
  relative response assigned to the same sample changes, even though nothing
  about the samples themselves changed.

You can reproduce both observations with:

```bash
python reproduce.py
```

See `reproduction.md` for the report contract.

Please inspect the source and public workflow, figure out
why the computed relative responses disagree with their definition, and
repair the implementation so that the analysis conforms to the documented
definition for all valid inputs — any saved response matrix and any sample
metadata table a user could legitimately provide. Do not hard-code specific
sample identities, batch layouts, orderings, or expected outputs.
