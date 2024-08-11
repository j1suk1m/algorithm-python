from sys import stdin

def dynamic_programming(N: int) -> int:
    dp = [0] * (N + 1)
    
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    
    for number in range(4, N + 1):
        dp[number] = dp[number - 2] + dp[number - 3]
        
    return dp[N]
    
T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    
    if N <= 3:
        print(1)
    else:
        print(dynamic_programming(N))