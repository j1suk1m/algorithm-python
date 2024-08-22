from sys import stdin

input = lambda: stdin.readline().rstrip()

while True:
    N = int(input())
    
    if N == 0:
        break
    elif N == 1:
        print(int(input()))
    else:
        P = [0] + list(int(input()) for _ in range(N))
        dp = [0] * (N + 1)
        dp[1] = P[1]
        
        for day in range(2, N + 1):
            dp[day] = max(P[day], P[day] + dp[day - 1])
            
        print(max(dp[1:]))