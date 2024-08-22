from sys import stdin

input = lambda: stdin.readline().rstrip()
dp = [[0] * 10 for _ in range(65)] 
dp[1] = [1] * 10

for i in range(2, 65):
    for j in range(10):
        for k in range(j, 10):
            dp[i][k] += dp[i - 1][j]
            
T = int(input())

for _ in range(T):
    N = int(input())
    print(sum(dp[N]))