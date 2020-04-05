def numbers_with_paren(numbers):
    open_paren = 0
    output = ""
    for n in numbers:
        number = int(n)
        if number > open_paren:
            opened_paren = number - open_paren
            output += '(' * (opened_paren)
            open_paren += opened_paren
        elif number < open_paren:
            closed_paren = open_paren - number
            output += ')' * (closed_paren)
            open_paren -= closed_paren
        output += str(number)
    if open_paren > 0:
        output += ')' * open_paren

    return output


test_case_count = int(input())
for i in range(test_case_count):
    numbers = [int(n) for n in input()]
    print("Case #{}: {}".format(i + 1, numbers_with_paren(numbers)))
