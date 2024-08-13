from sys import stdin

n = int(stdin.readline().rstrip())
boxes = [0] + list(map(int, stdin.readline().rstrip().split()))
dp = [1] * (n + 1)

for current in range(1, n + 1):
    for rest in range(1, current):
        if boxes[current] > boxes[rest]:
            dp[current] = max(dp[current], dp[rest] + 1)
            
print(max(dp))