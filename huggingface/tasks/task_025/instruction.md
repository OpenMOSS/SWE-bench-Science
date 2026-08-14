# Repair inconsistent cross-protocol Osprey validation reports

A spectroscopy group is validating a historical Osprey snapshot with
deterministic checkpoints derived from one synthetic phantom study. All runs
complete and produce finite values, but two independent report panels are not
compatible across supported acquisition configurations:

- a model-derived contribution changes substantially between edited
  acquisition encodings that represent the same calibration;
- a downstream quantitative result changes substantially between acquisition
  settings prepared to represent the same control.

Run the public reproduction, inspect the project source, checkpoints, and data
structures, and repair the scientific
implementation. A valid repair must preserve legitimate dependence on sequence
design, basis content, fitted signals, acquisition metadata, field strength,
and supported correction models.

Do not hard-code the visible records, replace either report with a fixed value,
or edit generated outputs.
