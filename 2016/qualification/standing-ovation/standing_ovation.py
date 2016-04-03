import sys


class StandingOvation:
    def __init__(self, audience):
        self.audience = audience

    def solve(self):
        total_standing = 0
        invites = 0
        for current_shyness, number_guests in enumerate(self.audience):
            if not number_guests:
                continue
            if current_shyness <= total_standing:
                total_standing += number_guests
            else:
                missing = (current_shyness - total_standing)
                invites += missing
                total_standing += (missing + number_guests)

        return invites


class Solver:
    def __init__(self, input_file):
        self.standing_ovations = []

        number_test_cases = int(input_file.readline())
        for _ in range(number_test_cases):
            audience_string = input_file.readline().strip().split(" ")[1:][0]
            self.standing_ovations.append(StandingOvation([int(x) for x in audience_string]))

    def solve_all(self):
        for standing_ovation in self.standing_ovations:
            yield standing_ovation.solve()


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        solver = Solver(f)

    for i, solution in enumerate(solver.solve_all()):
        print("Case #%d: %d" % (i + 1, solution))
