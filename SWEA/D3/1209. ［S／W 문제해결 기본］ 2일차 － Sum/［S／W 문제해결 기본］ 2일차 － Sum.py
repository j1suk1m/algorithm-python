T = 10
side_length = 100
results = []

for _ in range(T):
    ### 행의 합 100개, 열의 합 100개, 왼쪽 위 -> 오른쪽 아래 대각선의 합, 오른쪽 위 -> 왼쪽 아래 대각선의 합
    maximum_candidates = [0] * 202 
    test_case_number = int(input().rstrip())
    matrix = list(list(map(int, input().rstrip().split())) for _ in range(side_length))

    for row in range(side_length):
        for col in range(side_length):
            current_number = matrix[row][col]

            ### 행의 합
            maximum_candidates[row] += current_number

            ### 열의 합
            maximum_candidates[side_length + col] += current_number

            ### 왼쪽 위 -> 오른쪽 아래 대각선의 합
            if row == col:
                maximum_candidates[-2] += current_number

            ### 오른쪽 위 -> 왼쪽 아래 대각선의 합
            elif row + col == side_length - 1:
                maximum_candidates[-1] += current_number

    results.append(max(maximum_candidates))

for test_case_number in range(T):
    print("#{} {}".format(test_case_number + 1, results[test_case_number]))