from sys import stdin

def dynamic_programming(sugar: int) -> int:
    dp = [5000] * (sugar + 1)
    
    dp[3] = 1
    dp[5] = 1
    
    for bag in range(6, sugar + 1):
        dp[bag] = min(dp[bag - 3], dp[bag - 5]) + 1

    return dp[bag] if dp[bag] < 5000 else -1
            
N = int(stdin.readline().rstrip())

if N == 3 or N == 5:
    print(1)
elif N == 4:
    print(-1)
else:
    print(dynamic_programming(N))