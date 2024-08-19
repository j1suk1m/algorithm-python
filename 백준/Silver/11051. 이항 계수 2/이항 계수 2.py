from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

if K == 0 or N == 1 or N == K:
    print(1)
else:
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    dp[1][0] = 1
    dp[1][1] = 1

    for row in range(2, N + 1):
        for col in range(0, K + 1):
            if col == 0 or row == col:
                dp[row][col] = 1
            else:
                dp[row][col] = (dp[row - 1][col - 1] + dp[row - 1][col]) % 10007
            
    print(dp[N][K])