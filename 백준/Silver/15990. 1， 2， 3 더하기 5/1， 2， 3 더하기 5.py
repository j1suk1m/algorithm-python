from sys import stdin

T = int(stdin.readline().rstrip())
dp = [[0] * (4) for _ in range(100001)] ### [0, 1, 2, 3으로 끝나는 경우의 수]의 리스트

dp[1][1] = 1
dp[2][2] = 1
dp[3] = [0, 1, 1, 1]

for number in range(4, 100001):
    dp[number][1] = (dp[number - 1][2] + dp[number - 1][3]) % 1000000009
    dp[number][2] = (dp[number - 2][1] + dp[number - 2][3]) % 1000000009
    dp[number][3] = (dp[number - 3][1] + dp[number - 3][2]) % 1000000009
    
for _ in range(T):
    n = int(stdin.readline().rstrip())
    
    print(sum(dp[n]) % 1000000009)