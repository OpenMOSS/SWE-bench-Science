#!/usr/bin/env python3
"""Generate the task-local topology and building-unit libraries."""

from __future__ import annotations

import gzip
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def slot(coords: list[list[float]], tags: list[int], group: int) -> dict[str, object]:
    return {
        "species": ["X"] * len(coords),
        "coords": coords,
        "tags": tags,
        "pointgroup": "D*h" if len(coords) == 2 else "Oh",
        "equivalence_class": group,
    }


def chain(name: str, x_offset: float) -> dict[str, object]:
    cell = [[10.0, 0.0, 0.0], [0.0, 10.0, 0.0], [x_offset, 0.0, 8.0]]
    return {
        "cell": cell,
        "spacegroup_number": None,
        "slots": [
            slot([[0.0, 0.0, 1.0], [0.0, 0.0, -1.0]], [1, 4], 0),
            slot([[0.0, 0.0, 1.0], [0.0, 0.0, 3.0]], [1, 2], 1),
            slot([[0.0, 0.0, 3.0], [0.0, 0.0, 5.0]], [2, 3], 0),
            slot([[0.0, 0.0, 5.0], [0.0, 0.0, 7.0]], [3, 4], 2),
        ],
        "benchmark_description": f"independently authored periodic chain {name}",
    }


def pinned_control() -> dict[str, object]:
    center = [2.0, 2.0, 2.0]
    node = [
        [2.5, 2.0, 2.0], [1.5, 2.0, 2.0],
        [2.0, 2.5, 2.0], [2.0, 1.5, 2.0],
        [2.0, 2.0, 2.5], [2.0, 2.0, 1.5],
    ]
    return {
        "cell": [[4.0, 0.0, 0.0], [0.0, 4.0, 0.0], [0.0, 0.0, 4.0]],
        "spacegroup_number": None,
        "slots": [
            slot(node, [1, 2, 3, 4, 5, 6], 0),
            slot([[2.5, 2.0, 2.0], [5.5, 2.0, 2.0]], [1, 2], 1),
            slot([[2.0, 2.5, 2.0], [2.0, 5.5, 2.0]], [3, 4], 1),
            slot([[2.0, 2.0, 2.5], [2.0, 2.0, 5.5]], [5, 6], 1),
        ],
        "benchmark_description": "independently authored pinned periodic node",
    }


def write_topologies() -> None:
    names = ("etb-e", "sra", "unc", "pts", "tbo", "sod")
    payload = {
        "format_version": 1,
        "topologies": {
            **{name: chain(name, index * 0.08) for index, name in enumerate(names)},
            "pcu": pinned_control(),
        },
    }
    data = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode()
    with ROOT.joinpath("topologies.json.gz").open("wb") as raw:
        with gzip.GzipFile(filename="topologies.json", mode="wb", fileobj=raw, mtime=0) as archive:
            archive.write(data)


def write_building_units() -> None:
    text = """3
name=Benchmark_linker_linear pbc=\"F F F\"
X 0.0 0.0 -1.5
C 0.0 0.0 0.0
X 0.0 0.0 1.5
7
name=Benchmark_node_octahedral pbc=\"F F F\"
Zn 0.0 0.0 0.0
X 1.5 0.0 0.0
X -1.5 0.0 0.0
X 0.0 1.5 0.0
X 0.0 -1.5 0.0
X 0.0 0.0 1.5
X 0.0 0.0 -1.5
"""
    ROOT.joinpath("defaults.xyz").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_topologies()
    write_building_units()
