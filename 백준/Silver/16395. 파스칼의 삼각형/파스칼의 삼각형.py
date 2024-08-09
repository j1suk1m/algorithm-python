from sys import stdin

def dynamic_programming(dp: list, row_num: int, col_num: int) -> int:
    dp[1][1] = 1 
    dp[2][1] = 1
    dp[2][2] = 1
   
    for row in range(3, row_num + 1):
        for col in range(1, row + 1):
            if col == 1 or col == row:
                dp[row][col] = 1
            else:
                dp[row][col] = dp[row - 1][col - 1] + dp[row - 1][col]
                
    return dp[row_num][col_num]

n, k = map(int, stdin.readline().rstrip().split())    
dp = [[0] * (n + 1) for _ in range(n + 1)]

if k == 1 or n == k:
    print(1)
else:
    print(dynamic_programming(dp, n, k))