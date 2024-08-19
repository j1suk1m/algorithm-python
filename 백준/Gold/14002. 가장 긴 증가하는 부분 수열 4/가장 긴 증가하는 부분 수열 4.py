from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
A = [0] + list(map(int, input().split()))
dp = [[number] for number in A] 

for current in range(1, N + 1):
    for rest in range(1, current):
        if A[current] > A[rest]:
            if len(dp[current]) < len(dp[rest] + [A[current]]):
                dp[current] = dp[rest] + [A[current]]
            
dp = sorted(dp, key=lambda x: (-len(x), -sum(x)))

print(len(dp[0]))
print(*dp[0])