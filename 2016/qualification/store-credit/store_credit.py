import sys
from itertools import islice


class TestCase:
    def __init__(self, credit, item_count, items):
        self.credit = credit
        self.item_count = item_count
        self.items = items

    def __str__(self):
        return "Credit: %d, Items: %s" % (self.credit, self.items)


class Solver:
    def __init__(self, input_file):
        self.test_cases = []

        number_test_cases = int(input_file.readline())
        for _ in range(0, number_test_cases):
            self._parse_test_case(input_file)

    def solve(self):
        solutions = []
        for test_case in self.test_cases:
            solutions.append(self._solve_test_case(test_case))
        return solutions

    def _solve_test_case(self, test_case):
        for i, first in enumerate(test_case.items):
            for j in range(i + 1, len(test_case.items)):
                second = test_case.items[j]
                if (first + second) == test_case.credit:
                    return i + 1, j + 1

    def _parse_test_case(self, input_file):
        credit, item_count, items = [input_file.readline().strip() for _ in range(3)]
        self.test_cases.append(TestCase(int(credit), int(item_count), [int(x) for x in items.split(" ")]))


def solve(input_path):
    with open(input_path, "r") as input_file:
        solutions = Solver(input_file).solve()

    for i, solution in enumerate(solutions):
        print("Case #%d: %d %d" % (i + 1, solution[0], solution[1]))


if __name__ == '__main__':
    solve(sys.argv[1])
