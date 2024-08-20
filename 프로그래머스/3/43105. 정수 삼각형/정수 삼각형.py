def solution(triangle):
    triangle = [[0]] + [([0] + row) for row in triangle]
    dp = [[0] * (num + 1) for num in range(len(triangle))]
    
    dp[1][1] = triangle[1][1]
    
    for row in range(1, len(triangle) - 1):
        for col in range(1, row + 1):
            dp[row + 1][col] = max(dp[row + 1][col], dp[row][col] + triangle[row + 1][col])
            dp[row + 1][col + 1] = max(dp[row + 1][col + 1], dp[row][col] + triangle[row + 1][col + 1])
                
    answer = max(dp[-1])
    
    return answer