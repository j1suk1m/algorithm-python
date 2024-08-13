from sys import stdin

n = int(stdin.readline().rstrip())
triangle = [[0]] + list(([0] + list(map(int, stdin.readline().rstrip().split()))) for _ in range(n))

if n == 1:
    print(triangle[1][1])
else:
    dp = [[0] * (number + 1) for number in range(n + 1)]
    
    dp[1][1] = triangle[1][1]

    for row in range(1, n):
        for col in range(1, row + 1):
            current_sol = dp[row][col]
            next_left_sol = dp[row + 1][col]
            next_right_sol = dp[row + 1][col + 1]
            next_left_number = triangle[row + 1][col]
            next_right_number = triangle[row + 1][col + 1]
            
            dp[row + 1][col] = max(next_left_sol, next_left_number + current_sol)
            dp[row + 1][col + 1] = max(next_right_sol, next_right_number + current_sol)
                    
    print(max(dp[n]))