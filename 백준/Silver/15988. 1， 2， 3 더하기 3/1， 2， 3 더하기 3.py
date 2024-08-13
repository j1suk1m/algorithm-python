from sys import stdin

T = int(stdin.readline().rstrip())
dp = [0] * (1000001)

dp[1] = 1 ### 1
dp[2] = 2 ### 1 + 1, 2
dp[3] = 4 ### 1 + 3, 1 + 1 + 1, 2 + 1, 3

for number in range(4, 1000001):
    dp[number] = (dp[number - 1] + dp[number - 2] + dp[number - 3]) % 1000000009
    
for _ in range(T):
    n = int(stdin.readline().rstrip())
    
    print(dp[n])