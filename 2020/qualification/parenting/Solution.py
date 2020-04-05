def assign_activities(activities):
    assigned_activities = []
    c_busy_until = 0
    j_busy_until = 0
    activities.sort(key=lambda x: x[1])
    for i, start, end in activities:
        if start >= c_busy_until:
            assigned_activities.append((i, "C"))
            c_busy_until = end
        elif start >= j_busy_until:
            assigned_activities.append((i, "J"))
            j_busy_until = end
        else:
            return "IMPOSSIBLE"
    assigned_activities.sort(key=lambda x: x[0])
    return [a[1] for a in assigned_activities]


test_case_count = int(input())
for i in range(test_case_count):
    activities_count = int(input())
    activities = []
    for j in range(activities_count):
        start_end = input().split(' ')
        activities.append((j, int(start_end[0]), int(start_end[1])))
    schedule = assign_activities(activities)
    print("Case #{}: {}".format(i + 1, ''.join(schedule)))

