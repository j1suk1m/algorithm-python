from sys import stdin

def dynamic_programming(dp: list, tile: int) -> int:        
    for order in range(3, tile + 1):
        dp[order] = dp[order - 1] + dp[order - 2]
        
    return 2 * (2 * dp[tile] + dp[tile - 1])

N = int(stdin.readline().rstrip())
dp = [0] * 81

dp[1] = 1
dp[2] = 1

if N <= 2:
    print(2 * (2 * dp[N] + dp[N - 1]))
else:
    print(dynamic_programming(dp, N))