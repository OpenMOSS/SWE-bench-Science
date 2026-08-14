# Repair an incomplete stiff-kinetics campaign

A kinetics group is replaying a supplied multi-condition Robertson reaction
campaign with a historical SciPy source snapshot. The reaction systems,
initial compositions, rate constants, observation levels, time horizons, and
tolerances are valid. The campaign should produce one finite, mass-conserving
observation for every configured protocol and a stable aggregate summary. The
supplied implementation completes only part of the campaign, so the aggregate
result cannot be released.

Run the offline reproduction, inspect the scientific workflow and source, and
repair the implementation so that
the complete campaign is scientifically consistent. The repair must generalize
beyond the public protocols to other supported differential-equation systems,
integration directions, sampling choices, tolerances, and solver
configurations. Do not hard-code protocol identifiers, public rates, monitored
levels, or report fields, and do not modify the supplied scientific inputs.
