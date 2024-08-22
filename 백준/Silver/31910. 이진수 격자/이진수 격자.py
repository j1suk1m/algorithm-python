from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())

grid = [["0"] * (N + 1)] + list((["0"] + list(map(str, input().split()))) for _ in range(N))
dp = [[0] * (N + 1) for _ in range(N + 1)]

### 다이나믹 프로그래밍
for x in range(1, N + 1):
    for y in range(1, N + 1):
        left_number = dp[x][y - 1]
        above_number = dp[x - 1][y]
        dp[x][y] = int(format(max(left_number, above_number), 'b') + grid[x][y], 2)
        
print(dp[N][N])