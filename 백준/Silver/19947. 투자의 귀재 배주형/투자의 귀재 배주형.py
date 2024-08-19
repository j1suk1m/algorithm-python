from sys import stdin

input = lambda: stdin.readline().rstrip()

H, Y = map(int, input().split())
interest_rate = {1: 0.05, 3: 0.2, 5: 0.35}

if Y == 0:
    print(H)
elif Y == 1 or Y == 3 or Y == 5:
    print(int(H * (1 + interest_rate[Y])))
else:
    dp = [H] * (Y + 1)
    dp[1] = int(H * (1 + interest_rate[1]))

    for year in range(2, Y + 1):
        dp[year] = int(dp[year - 1] * (1 + interest_rate[1]))
        
        if year >= 5:
            dp[year] = int(max(dp[year], dp[year - 5] * (1 + interest_rate[5])))
        if year >= 3:
            dp[year] = int(max(dp[year], dp[year - 3] * (1 + interest_rate[3])))
            
    print(dp[Y])