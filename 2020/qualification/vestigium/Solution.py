def trace_and_dupes(mat):
    n = len(mat)
    mat_trace = 0
    rows_with_dupes = 0
    columns_with_dupes = 0
    cols = {}
    for i in range(n):
        row = set()
        for j in range(n):
            elem = mat[i][j]
            if j not in cols:
                cols[j] = set()
            cols[j].add(elem)
            if i == j:
                mat_trace += elem
            row.add(elem)
        if len(row) < n:
            rows_with_dupes += 1
    for column in cols.values():
        if len(column) < n:
            columns_with_dupes += 1

    return mat_trace, rows_with_dupes, columns_with_dupes


def matrices_from_input():
        yield mat


test_case_count = int(input())
for i in range(test_case_count):
    row_count = int(input())
    mat = []
    for _ in range(row_count):
        row = input()
        mat.append([int(e) for e in row.split(" ")])
    trace, rows, columns = trace_and_dupes(mat)
    print("Case #{}: {} {} {}".format(i + 1, trace, rows, columns))
