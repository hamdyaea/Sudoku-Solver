#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
"""Solve 9×9 Sudoku puzzles without NumPy or interactive prompts."""
from __future__ import annotations

import argparse
from pathlib import Path

Grid = list[list[int]]
EXAMPLE: Grid = [
    [0, 4, 1, 6, 5, 0, 2, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 7],
    [7, 0, 2, 0, 0, 0, 5, 6, 3],
    [0, 0, 0, 2, 0, 8, 0, 0, 1],
    [4, 0, 0, 0, 7, 0, 0, 0, 5],
    [1, 0, 0, 4, 0, 5, 0, 0, 0],
    [2, 3, 4, 0, 0, 0, 1, 0, 6],
    [8, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 9, 0, 4, 6, 3, 2, 0],
]


def validate(grid: Grid) -> None:
    if len(grid) != 9 or any(len(row) != 9 for row in grid):
        raise ValueError("A Sudoku grid must contain exactly 9 rows of 9 values")
    if any(type(value) is not int or not 0 <= value <= 9 for row in grid for value in row):
        raise ValueError("Cells must be integers from 0 to 9")
    groups = list(grid) + [[grid[r][c] for r in range(9)] for c in range(9)]
    groups += [[grid[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]
               for br in (0, 3, 6) for bc in (0, 3, 6)]
    for group in groups:
        nonzero = [x for x in group if x]
        if len(nonzero) != len(set(nonzero)):
            raise ValueError("Conflicting clues in the puzzle")


def candidates(grid: Grid, row: int, col: int) -> set[int]:
    used = set(grid[row])
    used.update(grid[r][col] for r in range(9))
    used.update(grid[r][c] for r in range(row // 3 * 3, row // 3 * 3 + 3)
                for c in range(col // 3 * 3, col // 3 * 3 + 3))
    return set(range(1, 10)) - used


def solve(grid: Grid) -> Grid | None:
    """Return one solution, or None. The input grid is never modified."""
    validate(grid)
    board = [row.copy() for row in grid]

    def backtrack() -> bool:
        empty = [(r, c) for r in range(9) for c in range(9) if board[r][c] == 0]
        if not empty:
            return True
        row, col = min(empty, key=lambda cell: len(candidates(board, *cell)))
        for number in sorted(candidates(board, row, col)):
            board[row][col] = number
            if backtrack():
                return True
        board[row][col] = 0
        return False

    return board if backtrack() else None


def parse_grid(text: str) -> Grid:
    values = [ch for ch in text if ch in "0123456789."]
    if len(values) != 81:
        raise ValueError("Expected exactly 81 cells (0 or . for empty)")
    grid = [[0 if ch == "." else int(ch) for ch in values[i:i + 9]]
            for i in range(0, 81, 9)]
    validate(grid)
    return grid


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", nargs="?", type=Path, help="Puzzle file containing 81 cells")
    args = parser.parse_args()
    try:
        puzzle = parse_grid(args.file.read_text(encoding="utf-8")) if args.file else EXAMPLE
        result = solve(puzzle)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    if result is None:
        parser.exit(1, "No solution exists.\n")
    for row in result:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
