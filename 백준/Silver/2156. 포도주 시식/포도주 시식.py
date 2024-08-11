from sys import stdin

def dynamic_programming(n: int, wines: list) -> int:
    dp = [0] * (n + 1)
    
    dp[1] = wines[1]
    dp[2] = wines[1] + wines[2]
    
    for wine in range(3, n + 1):
        dp[wine] = max(dp[wine - 2] + wines[wine],
                       dp[wine - 3] + wines[wine - 1] + wines[wine], 
                       dp[wine - 1]) 

    return max(dp)

n = int(stdin.readline().rstrip())
wines = [0] + list(int(stdin.readline().rstrip()) for _ in range(n))

if n <= 2:
    print(sum(wines))
else:
    print(dynamic_programming(n, wines))