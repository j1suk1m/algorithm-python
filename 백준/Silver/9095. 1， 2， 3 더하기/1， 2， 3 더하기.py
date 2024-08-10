from sys import stdin

def dynamic_programming(n: int) -> int:
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    
    for number in range(4, n + 1):
        dp[number] = dp[number - 1] + dp[number - 2] + dp[number - 3]
        
    return dp[n]
    
T = int(stdin.readline().rstrip())

for _ in range(T):
    n = int(stdin.readline().rstrip())

    if n <= 2:
        print(n)
    elif n == 3:
        print(4)
    else:
        print(dynamic_programming(n))