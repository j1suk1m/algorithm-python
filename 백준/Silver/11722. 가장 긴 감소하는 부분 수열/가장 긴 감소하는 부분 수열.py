from sys import stdin

N = int(stdin.readline().rstrip())
A = [0] + list(map(int, stdin.readline().rstrip().split()))
dp = [1] * (N + 1)

for current in range(N, 0, -1):
    for rest in range(N, current, -1):
        if A[current] > A[rest]:
            dp[current] = max(dp[current], dp[rest] + 1)

print(max(dp[1:]))