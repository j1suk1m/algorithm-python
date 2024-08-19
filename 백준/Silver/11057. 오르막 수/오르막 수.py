from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
dp = [[0] * 10 for _ in range(N + 1)] 

dp[1] = [1] * 10

for length in range(2, N + 1):
    for number in range(10):
        dp[length][number] = (dp[length][number - 1] + dp[length - 1][number]) % 10007
        
print(sum(dp[N]) % 10007)