#!/usr/bin/env python3
"""Generate the minimal, benchmark-authored magnetic-operation catalogue."""

from __future__ import annotations

import sqlite3
from pathlib import Path


OUTPUT = Path(__file__).with_name("symm_data_magnetic.sqlite")


def operation_blob(point_operator: int, translation: tuple[int, int, int], denominator: int) -> bytes:
    return bytes((point_operator, *translation, denominator, 1))


def build(path: Path = OUTPUT) -> None:
    if path.exists():
        path.unlink()
    database = sqlite3.connect(path)
    cursor = database.cursor()
    cursor.execute(
        """CREATE TABLE space_groups (
        magtype integer, BNS1 integer, BNS2 integer, BNS_label text,
        OG1 integer, OG2 integer, OG3 integer primary key, OG_label text,
        OG_BNS_transform blob, BNS_symops blob, BNS_lattice blob,
        BNS_Wyckoff blob, OG_symops blob, OG_lattice blob, OG_Wyckoff blob
        )"""
    )
    cursor.execute(
        """CREATE TABLE point_operators (
        idx integer, hex integer, symbol text, matrix text, string text
        )"""
    )
    cursor.execute("CREATE TABLE credit (credit text)")
    cursor.executemany(
        "INSERT INTO point_operators VALUES (?, ?, ?, ?, ?)",
        [
            (0, 0, "1", "1,0,0,0,1,0,0,0,1", "x,y,z"),
            (3, 0, "2z", "-1,0,0,0,-1,0,0,0,1", "-x,-y,z"),
        ],
    )
    identity = operation_blob(1, (0, 0, 0), 1)
    half_x_twofold = operation_blob(4, (1, 0, 0), 2)
    third_y_twofold = operation_blob(4, (0, 1, 0), 3)
    lattice = bytes((1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1))
    rows = [
        ((4, 4, 11, "benchmark_4.11", 4, 11, 1, "benchmark_4.11"), identity + half_x_twofold),
        ((4, 4, 9, "benchmark_4.9", 4, 9, 2, "benchmark_4.9"), identity + third_y_twofold),
    ]
    for prefix, operators in rows:
        cursor.execute(
            "INSERT INTO space_groups VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (*prefix, b"", operators, lattice, b"", b"", lattice, b""),
        )
    cursor.execute(
        "INSERT INTO credit VALUES (?)",
        (
            "Synthetic catalogue authored for OpenMOSS SWE-bench Science; "
            "not copied from ISO-MAG or a magnetic-group table.",
        ),
    )
    database.commit()
    database.close()


if __name__ == "__main__":
    build()
