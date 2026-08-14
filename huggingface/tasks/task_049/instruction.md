# Restore the stochastic sampling and discretization contract

A computational physics group is maintaining the supplied historical py-pde
source. Complete stochastic `PDE.solve()` calculations remain numerically
stable because the current implementation compensates one scaling choice with
another. The defect is instead at the reusable interface between Gaussian
sampling and spatial discretization.

The backend Gaussian primitive is a standard-normal sampling service. For the
same backend, seed, dtype, and array shape, its draw must not change when only
the physical grid measure changes. Cell volumes belong to the discretization
of a stochastic field: a variance-based solver converts continuum noise
variance to a cell increment using the inverse cell measure. Keeping these
responsibilities separate lets the primitive remain reusable across fields and
backends while solvers consistently interpret the public noise variance.

The package also documents a lower-level direct-realization interface. A user
who chooses that route supplies the complete spatially discretized realization,
including any required measure factor. That does not change the contract of the
backend standard-normal primitive used by variance-based solvers.

Run the offline reproduction, inspect the task context and complete source
snapshot, and repair the implementation so that both sides of this contract
hold for all supported valid inputs. Preserve deterministic PDE
behavior, public APIs, stochastic interpretations, supported backends, device
and dtype behavior, and unrelated functionality.

Do not hard-code the public grids, seeds, controlled draw, lifecycle status, or
generated report. The public experiment states the architecture being studied
but does not name a target source file or prescribe a patch shape. Hidden tests
vary geometry, backend, solver, noise interpretation, and realization route.
