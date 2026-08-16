from __future__ import annotations

import sys
from pathlib import Path


TASK_DIR = Path(__file__).resolve().parents[1]
SOURCE_DIR = TASK_DIR / "source"
FIXTURE_DIR = TASK_DIR / "fixtures"


def _energy(stem: str) -> float:
    sys.path.insert(0, str(SOURCE_DIR))

    import openmm
    import openmm.app

    coordinates = openmm.app.GromacsGroFile(str(FIXTURE_DIR / f"{stem}.gro"))
    topology = openmm.app.GromacsTopFile(str(FIXTURE_DIR / f"{stem}.top"))
    system = topology.createSystem(
        nonbondedMethod=openmm.app.NoCutoff,
        switchDistance=None,
        constraints=None,
    )
    integrator = openmm.VerletIntegrator(1 * openmm.unit.femtosecond)
    context = openmm.Context(
        system,
        integrator,
        openmm.Platform.getPlatformByName("Reference"),
    )
    context.setPositions(coordinates.positions)
    value = context.getState(getEnergy=True).getPotentialEnergy().value_in_unit(
        openmm.unit.kilojoules_per_mole
    )
    return float(value)


def calculate_energies() -> dict[str, float]:
    return {
        stem: _energy(stem)
        for stem in ("combination_rule_1", "combination_rule_3")
    }
