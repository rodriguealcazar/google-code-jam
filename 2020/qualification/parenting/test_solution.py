import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from solution import assign_activities, main


class TestAssignActivities(unittest.TestCase):

    def test_simple_alternation(self):
        test_activities = [
            (1, 360, 480),
            (2, 420, 540),
            (3, 600, 660)
        ]
        self.assertEqual(
            ['C', 'J', 'C'],
            assign_activities(test_activities))

    def test_impossible_case(self):
        test_activities = [
            (1, 0, 1440),
            (2, 1, 3),
            (3, 2, 4)
        ]
        self.assertEqual(
            "IMPOSSIBLE",
            assign_activities(test_activities)
        )

    def test_larger_example(self):
        test_activities = [
            (1, 99, 150),
            (2, 1, 100),
            (3, 100, 301),
            (4, 2, 5),
            (5, 150, 250)
        ]
        self.assertEqual(
            ['J', 'C', 'C', 'J', 'J'],
            assign_activities(test_activities)
        )

    def test_any_combination_possible(self):
        test_activities = [
            (1, 0, 720),
            (2, 720, 1440)
        ]
        self.assertEqual(
            ['C', 'C'],
            assign_activities(test_activities)
        )


class TestFullInput(unittest.TestCase):

    def test_sample_input(self):
        sample_input = (
            "4\n",
            "3\n",
            "360 480\n",
            "420 540\n",
            "600 660\n",
            "3\n",
            "0 1440\n",
            "1 3\n",
            "2 4\n",
            "5\n",
            "99 150\n",
            "1 100\n",
            "100 301\n",
            "2 5\n",
            "150 250\n",
            "2\n",
            "0 720\n",
            "720 1440\n"
        )
        expected_output = (
            "Case #1: CJC\n" +
            "Case #2: IMPOSSIBLE\n" +
            "Case #3: JCCJJ\n" +
            "Case #4: CC\n"
        )

        mock_stdout = StringIO()
        with patch('builtins.input', side_effect=sample_input):
            with redirect_stdout(mock_stdout):
                main()

        self.assertEqual(expected_output, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
