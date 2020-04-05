import math
from itertools import tee


def int_to_digits(n):
    digits = []
    for i in range(int(math.log10(n)) + 1):
        digits.insert(0, n % 10)
        n //= 10
    return digits


def digits_to_int(digits):
    n = 0
    for i, d in enumerate(digits[::-1]):
        n += (d * (10**i))
    return n


def is_tidy(digits):
    return all(map(lambda t: t[0] <= t[1], pairwise(digits)))


def pairwise(digits):
    a, b = tee(digits)
    next(b, None)
    return zip(a, b)


def reduce(digits):
    for i in range(len(digits)):
        current_d = digits[i]
        next_d = digits[i + 1]
        if (current_d > next_d):
            digits = (
                digits[:i] +
                [current_d - 1] +
                [9] * (len(digits) - (i + 1))
            )
            break

    return digits


def find_last_tidy(n):
    digits = int_to_digits(n)
    while not is_tidy(digits):
        digits = reduce(digits)
    return digits_to_int(digits)


def parse_input(f):
    number_cases = int(f.readline())
    for i in range(number_cases):
        print(
            "Case #{}: {}".format(i + 1, find_last_tidy(int(f.readline())))
        )

if __name__ == "__main__":
    import sys
    with open(sys.argv[1]) as f:
        parse_input(f)
