from sys import stdin

def dynamic_programming(N: int) -> int:
    dp = [0] * (N + 1)
    coins = [2, 5, 7]
    
    dp[1] = 1
    dp[2] = 1

    for money in range(3, N + 1):
        dp[money] = dp[money - 1] + 1
        
        for coin in coins:
            if money >= coin:
                dp[money] = min(dp[money], dp[money - coin] + 1)
                
    return dp[N]

N = int(stdin.readline().rstrip())

if N == 0:
    print(0)
elif N == 1 or N == 2 or N == 5 or N == 7:
    print(1)
else:
    print(dynamic_programming(N))