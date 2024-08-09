from sys import stdin

def dynamic_programming(target: int) -> int:
    dp = [1] * (n + 1)

    for number in range(4, target + 1):
        dp[number] = dp[number - 1] + dp[number - 3]
        
    return dp[target]

n = int(stdin.readline().rstrip())

if n <= 3:
    print(1)
else:
    print(dynamic_programming(n))