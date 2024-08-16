from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
things = [(0, 0)] + list(tuple(map(int, input().split())) for _ in range(N))
dp = [[0] * (K + 1) for _ in range(N + 1)]

for thing in range(1, N + 1):
    for weight in range(1, K + 1):
        thing_weight, thing_value = map(int, things[thing])
        
        if weight < thing_weight:
            dp[thing][weight] = dp[thing - 1][weight]
        else:
            dp[thing][weight] = max(dp[thing - 1][weight], dp[thing - 1][weight - thing_weight] + thing_value)

print(dp[N][K])