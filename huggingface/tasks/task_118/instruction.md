# Repair the periodic molecular calculation

A small research group uses the supplied high-level Python interface to compare
single-point energies for a heteroatom-rich molecular model in several valid
periodic-cell representations.  The calculations finish and return finite
values, but the results are not reliable enough for a scientific workflow.

Work only with the offline source snapshot in `source/`.  Use the public
reproduction command and the included method paper and API documentation to
understand the observations.  Repair the implementation so that equivalent
valid periodic representations give consistent scientific results while
preserving the public interfaces and units.

Do not change `reproduce.py` or hard-code its numbers.  Keep the fix general:
the same contract should hold beyond the displayed observation.  Stop and
report a runner failure if the offline build or calculation cannot be completed
rather than hiding it with fabricated output.
