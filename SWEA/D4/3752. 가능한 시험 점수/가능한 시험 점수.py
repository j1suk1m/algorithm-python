T = int(input())

for test_case in range(T):
    N = int(input())
    points_per_problem = list(map(int, input().split()))
    possible_points = {0}

    for point in points_per_problem:
        possible_point_candidates = list(map(lambda x: x + point, possible_points))
        possible_points.update(possible_point_candidates)

    print("#{} {}".format(test_case + 1, len(possible_points)))