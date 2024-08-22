from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
heights = list(map(int, input().split())) + [0]
dp = [0] * (N + 1) 

for idx in range(N - 1, -1, -1):
    height = heights[idx]
    
    if height > 0:
        if idx + height + 1 < N:
            dp[idx] = dp[idx + height + 1] + 1
        else:
            dp[idx] = 1
    else:
        dp[idx] = dp[idx + 1] + 1
        
print(*dp[:-1])