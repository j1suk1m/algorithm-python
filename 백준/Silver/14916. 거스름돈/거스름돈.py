from sys import stdin

def dynamic_programming(money: int) -> int:
    dp = [100000] * (money + 1)
    
    dp[2] = 1
    dp[4] = 2
    dp[5] = 1
    
    for coin in range(6, money + 1):
        dp[coin] = min(dp[coin - 2], dp[coin - 5]) + 1

    return dp[money] if dp[money] < 100000 else -1
            
n = int(stdin.readline().rstrip())

if n == 1 or n == 3:
    print(-1)
elif n == 2 or n == 5:
    print(1)
elif n == 4:
    print(2)
else:
    print(dynamic_programming(n))