from StringIO import StringIO
from unittest import TestCase

from standing_ovation import StandingOvation, Solver


class TestStandingOvation(TestCase):
    def test_case_1(self):
        self.assertEqual(0, StandingOvation([1, 1, 1, 1, 1]).solve())

    def test_case_2(self):
        self.assertEqual(1, StandingOvation([0, 9]).solve())

    def test_case_3(self):
        self.assertEqual(2, StandingOvation([1, 1, 0, 0, 1, 1]).solve())

    def test_case_4(self):
        self.assertEqual(0, StandingOvation([1]).solve())


class TestSover(TestCase):
    TEST_INPUT = """\
4
4 11111
1 09
5 110011
0 1
"""

    def test(self):
        test_input_file = StringIO(self.TEST_INPUT)
        self.assertEqual([0, 1, 2, 0], [solution for solution in Solver(test_input_file).solve_all()])
