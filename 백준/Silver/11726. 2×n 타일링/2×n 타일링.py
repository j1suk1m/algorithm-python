from sys import stdin

def dynamic_programming(n: int) -> int:
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 2
    
    for width in range(3, n + 1):
        dp[width] = dp[width - 1] + dp[width - 2]
        
    return dp[n]
    
n = int(stdin.readline().rstrip())

if n <= 2:
    print(n)
else:
    print(dynamic_programming(n) % 10007)