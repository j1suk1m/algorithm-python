from sys import stdin

T = int(stdin.readline().rstrip())
dp = [0] * 10001

dp[1] = 1
dp[2] = 1

for number in range(3, 10001):
    dp[number] = dp[number - 1] + dp[number - 2]

for test_case in range(1, T + 1):
    P, Q = map(int, stdin.readline().rstrip().split())
            
    print("Case #{}: {}".format(test_case, dp[P] % Q))