"""Minimal benchmark geometric types used by the synthetic task library.

These approximate radii and angles are independently selected compatibility
values. They are not the UFF or UFF4MOF parameter table.
"""

from __future__ import annotations

from typing import NamedTuple


class UFFType(NamedTuple):
    symbol: str
    radius: float
    angle: float
    coordination: int


UFF4MOF: tuple[UFFType, ...] = (
    UFFType("X_", 0.35, 180.0, 1),
    UFFType("H_", 0.37, 180.0, 1),
    UFFType("C_1", 0.77, 180.0, 2),
    UFFType("C_3", 0.77, 109.5, 4),
    UFFType("Zn6_benchmark", 1.22, 90.0, 6),
)
