import unittest

from tidy_numbers import find_last_tidy


class TestTidyNumbers(unittest.TestCase):

    def test_tidy(self):
        self.assertEqual(123, find_last_tidy(123))

    def test_simple_untidy(self):
        self.assertEqual(129, find_last_tidy(132))

    def test_single_digit(self):
        self.assertEqual(7, find_last_tidy(7))

    def test_lower_thousands(self):
        self.assertEqual(999, find_last_tidy(1000))

    def test_really_large(self):
        self.assertEqual(99999999999999999, find_last_tidy(111111111111111110))


if __name__ == '__main__':
    unittest.main()
