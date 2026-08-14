# Task 065

The supplied project is used to inspect fields reconstructed from particles in
hydrodynamic simulations. A normal analysis workflow completes on the bundled
workload and produces finite observations, but a reported scientific quantity
can change when the same particle data are used through another valid numerical
representation. This can affect comparisons between otherwise compatible
analyses rather than merely changing the appearance of a plot.

Read the accompanying method material and the local visualization notes. Run
the public reproduction first, then inspect the historical source and trace the
ordinary public workflows that load the particle data and construct the
observations. Repair the implementation so that the documented scientific
quantity is correct and stable for supported representations of the same
physical input.

The change must be a general repair to the project under `source/`. Do not
replace the workload, edit the public reproduction to hide the observation, or
hard-code its values. Use the supplied scientific definitions and the source's
public API to investigate the discrepancy, and validate the repair with input
variations of your own. Keep the public API usable and preserve valid behavior
outside the reported case.
