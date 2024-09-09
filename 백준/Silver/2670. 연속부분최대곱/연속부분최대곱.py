from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
numbers = [float(input()) for _ in range(N)]
dp = [0] * N
answer = 0.0

dp[0] = numbers[0]

for index in range(1, N):
    dp[index] = max(numbers[index], numbers[index] * dp[index - 1])
    answer = max(answer, dp[index])
    
print("{:.3f}".format(answer))