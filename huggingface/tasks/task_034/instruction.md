# Repair an inconsistent stochastic trajectory calculation

A research group is replaying the supplied noisy nonlinear-oscillator study
with a historical Diffrax source snapshot. The experiment uses a fixed ensemble
of prescribed stochastic controls and a valid reverse-oriented time interval.
The replay completes but the supplied implementation does not expose a
complete, inspectable ensemble for the configured reverse-time study.

Run the offline reproduction, inspect the complete source and accompanying
public experiment code, and repair the
scientific implementation so that the supported calculation is consistent.
The repair must generalize to other valid stochastic models, solver choices,
time intervals, and random controls supported by the project. Do not hard-code
the supplied ensemble, its aggregate result, or a fixture-specific outcome, and
do not modify the supplied study configuration or generated reports.
