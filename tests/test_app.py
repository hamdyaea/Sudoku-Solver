# Developer: Hamdy Abou El Anein
# Contact: info@daylightlinux.ch
# SPDX-License-Identifier: GPL-3.0-or-later
import importlib.util
from pathlib import Path
import unittest
spec=importlib.util.spec_from_file_location("app",Path(__file__).resolve().parents[1]/"SudokuSolver.py")
app=importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)
class Tests(unittest.TestCase):
    def test_example(self):
        solved=app.solve(app.EXAMPLE)
        self.assertIsNotNone(solved)
        self.assertTrue(all(0 not in row for row in solved))
        self.assertEqual(app.EXAMPLE[0][0],0)
        app.validate(solved)

    def test_conflicts(self):
        invalid=[row.copy() for row in app.EXAMPLE]
        invalid[0][0]=4
        with self.assertRaises(ValueError):app.solve(invalid)

    def test_parsing(self):
        grid=app.parse_grid("0"*81)
        self.assertEqual(len(grid),9)
        with self.assertRaises(ValueError):app.parse_grid("123")

if __name__=="__main__":unittest.main()
