from sys import stdin

def dynamic_programming(n: int) -> int:
    dp = [0] * (n + 1)
    
    dp[0] = 1
    dp[1] = 1

    for number in range(2, n + 1):
        dp[number] = (dp[number - 2] + dp[number - 1] + 1) % 1000000007
        
    return dp[n]

n = int(stdin.readline().rstrip())

if n <= 1:
    print(1)
else:
    print(dynamic_programming(n))