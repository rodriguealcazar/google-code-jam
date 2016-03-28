from StringIO import StringIO
from unittest import TestCase

from store_credit import Solver

TEST_INPUT = """\
3
100
3
5 75 25
200
7
150 24 79 50 88 345 3
8
8
2 1 9 4 4 56 90 3
"""


class TestSolver(TestCase):
    def test_solve(self):
        expected_solutions = [
            (2, 3),
            (1, 4),
            (4, 5)
        ]

        solutions = Solver(StringIO(TEST_INPUT)).solve()

        self.assertEqual(expected_solutions, solutions)
