Run `python reproduce.py` from this task directory and inspect the bundled
source snapshot and offline workbench.

The public workflow should expose a finite, inspectable diffusion-MRI
observation on the supplied local case, but the reported output is irregular
before repair. Repair the implementation in `source/` so the same workflow
produces a coherent result on the public case and on broader valid inputs.

Keep the repair general. Do not hard-code the supplied observation or change
the public runner, public metadata, or task directory layout.
