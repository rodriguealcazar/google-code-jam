import unittest

from solution import assign_activities


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

if __name__ == '__main__':
    unittest.main()
