from sys import stdin

def dynamic_programming(N: int) -> int:
    dp = [0] * (N + 1)
    
    dp[1] = 1
    dp[2] = 2
    
    for number in range(3, N + 1):
        dp[number] = (dp[number - 1] + dp[number - 2]) % 15746
        
    return dp[N]
    
N = int(stdin.readline().rstrip())

if N <= 2:
    print(N)
else:
    print(dynamic_programming(N))