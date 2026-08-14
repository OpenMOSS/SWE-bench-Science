# Repair a static structural-analysis workflow

The supplied Pynite source is an historical snapshot of a small structural
finite-element library.  The public workbench builds two legal frame
configurations and records their static-analysis observations.

One configuration is an ordinary restrained frame.  For the other legal
configuration, the historical snapshot can
nevertheless finish and report non-finite, implausibly large, or
solver-dependent values.  The official manual in `paper.md` supplies the
stability and solver definitions needed to interpret those observations.

Repair the historical workflow so it no longer silently presents a misleading
static result for configurations that the documented model semantics cannot
support, while retaining finite, consistent results for supported structures.
Keep the public analysis interfaces and their documented options usable.  Do
not replace the finite-element model with a fixture-specific answer or change
the public workbench to hide an observation.

Start by running `python reproduce.py`; the JSON output is an observation
workbench rather than a reference answer.  You may add your own small models
and tests while reasoning about the source.  The final implementation should
remain valid for additional supported structural models while retaining the
documented scientific contract.
