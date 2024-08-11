from sys import stdin

def dynamic_programming(n: int, m: int):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            if not (x == 1 and y == 1):
                dp[x][y] = (dp[x][y - 1] + dp[x - 1][y - 1] + dp[x - 1][y]) % 1000000007

    return dp[n][m]

n, m = map(int, stdin.readline().rstrip().split())

if n == 1 and m == 1:
    print(1)
else:
    print(dynamic_programming(n, m))