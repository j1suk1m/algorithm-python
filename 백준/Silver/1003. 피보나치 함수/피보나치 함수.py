from sys import stdin

def fibonacci(N: int) -> list:
    dp = [[0, 0] for _ in range(N + 1)] 
    
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    
    for number in range(2, N + 1):
        dp[number] = list(dp[number - 1][idx] + dp[number - 2][idx] for idx in range(2))
        
    return dp[N]

T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        print(*fibonacci(N))