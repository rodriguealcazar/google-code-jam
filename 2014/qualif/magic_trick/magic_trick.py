import io
import sys
import os.path

class InputReader:

    def __init__(self, input_file):
        self.input_file = input_file

    def parse_test(self):
        number_of_cases = int(self.input_file.readline())
        for i in range(number_of_cases):
            yield (self._parse_answer(),
                   self._parse_rows(),
                   self._parse_answer(),
                   self._parse_rows())

    def _parse_rows(self):
        return [set(self.input_file.readline().strip().split(' '))
                    for i in range(4)]

    def _parse_answer(self):
        return int(self.input_file.readline())


class Magician:

    def __init__(self, first_answer, first_rows, second_answer, second_rows):
        self.first_answer = first_answer
        self.first_rows = first_rows
        self.second_answer = second_answer
        self.second_rows = second_rows

    def solve(self):
        candidates = (
            self.first_rows[self.first_answer - 1]
            &
            self.second_rows[self.second_answer - 1]
        )

        number_candidates = len(candidates)
        if number_candidates == 1:
            return candidates.pop()
        elif number_candidates == 0:
            return "Volunteer cheated!"
        else:
            return "Bad magician!"


def solve(input_file):
    output = io.StringIO()
    counter = 1
    reader = InputReader(input_file)
    for test_input in reader.parse_test():
        magician = Magician(*test_input)
        test_result = magician.solve()
        output.write(u"Case #%i: %s\n" % (counter, test_result))
        counter += 1
    return output.getvalue()

if __name__ == "__main__":
    input_file_path = sys.argv[1]
    file_name = os.path.splitext(input_file_path)[0]
    results = solve(open(input_file_path, 'r'))
    with open(file_name + ".out", 'w') as output_file:
        output_file.write(results)
