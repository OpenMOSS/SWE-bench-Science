# Repair a seasonal fire-weather calculation

A climate-analysis group is reproducing a seasonal fire-weather workflow from
the complete historical source snapshot in `source/`. The workflow completes
on the supplied station histories and returns finite arrays, but its seasonal
trajectory is not consistent with the task's scientific definitions.

Use the source snapshot, `fixtures/seasonal_weather_case.json`, task context,
and the public reproduction to investigate the discrepancy. Run
`python reproduce.py` before and after your changes. Repair the project
implementation, not the scientific input or the public experiment.

Your solution must:

- preserve the documented public xarray-facing workflow and supported unit
  conversions;
- preserve the stateful interpretation of the FWI method when a seasonal mask
  changes over time;
- remain correct for other valid seasonal histories, initial states, masks,
  time layouts, and small spatial arrays;
- preserve ordinary continuous-season calculations when no seasonal gap is
  present; and
- avoid hard-coding this fixture, dates, station names, output values, or source
  filenames.

Inspect the scientific inputs and references, form and test your own
hypotheses, and repair the underlying implementation rather than manufacturing
agreement in the fixture, public experiment, or generated report. Do not
modify `fixtures/`, `reproduce.py`, or generated reports to hide a
source defect.
