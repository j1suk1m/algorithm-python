from sys import stdin

def dynamic_programming(n: int, m: int) -> int:
    dxs = [0, -1, -1]
    dys = [-1, -1, 0]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    dp[1][1] = 1

    for x in range(1, n + 1):
        for y in range(1, m + 1):
            for dx, dy in zip(dxs, dys):
                bx = x + dx 
                by = y + dy
                
                if (1 <= bx <= n and 1 <= by <= m):
                    dp[x][y] += (dp[bx][by] % 1000000007)
                    
            dp[x][y] %= 1000000007
                    
    return dp[n][m]

n, m = map(int, stdin.readline().rstrip().split())

if n == 1 and m == 1:
    print(1)
else:
    print(dynamic_programming(n, m))