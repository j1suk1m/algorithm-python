from sys import stdin

def dynamic_programming(N: int, stairs: list) -> int:
    dp = [0] * (N + 1)
    
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]
    
    for stair in range(3, N + 1):
        dp[stair] = max(dp[stair - 2], stairs[stair - 1] + dp[stair - 3]) + stairs[stair]

    return dp[N]

N = int(stdin.readline().rstrip())
stairs = [0] + list(int(stdin.readline().rstrip()) for _ in range(N))

if N <= 2:
    print(sum(stairs))
else:
    print(dynamic_programming(N, stairs))