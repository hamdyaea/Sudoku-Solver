# Sudoku Solver

A pure-Python 9×9 Sudoku solver with input validation and deterministic backtracking.

**Developer:** Hamdy Abou El Anein
**Contact:** info@daylightlinux.ch
**License:** GNU GPL v3 (see LICENSE).

## Highlights

- Python 3 standard library only; no EasyGUI or NumPy dependency.
- Explicit CLI options, validation and automated tests.
- Original implementation preserved in the [old branch](https://github.com/hamdyaea/Sudoku-Solver/tree/old).

## Run

    python3 SudokuSolver.py puzzle.txt

## Test

    python3 -m unittest discover -s tests -v
