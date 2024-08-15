from sys import stdin

N = int(stdin.readline().rstrip())
powers = [0] + list(map(int, stdin.readline().rstrip().split()))
dp = [1] * (N + 1)

for current in range(N, -1, -1):
    for rest in range(N, current, -1):
        if powers[current] > powers[rest]:
            dp[current] = max(dp[current], dp[rest] + 1)

print(N - max(dp[1:]))