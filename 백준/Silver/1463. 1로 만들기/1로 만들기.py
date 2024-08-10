from sys import stdin

def dynamic_programming(N: int) -> int:
    dp = [100001] * (N + 1)
    
    dp[1] = 0
    dp[2] = 1
    dp[3] = 1
    
    for number in range(4, N + 1):
        dp[number] = dp[number - 1] + 1
        
        if number % 3 == 0:
            dp[number] = min(dp[number], dp[number // 3] + 1)
        if number % 2 == 0:
            dp[number] = min(dp[number], dp[number // 2] + 1)
            
    return dp[N]
    
N = int(stdin.readline().rstrip())

if N == 1:
    print(0)
elif 2 <= N <= 3:
    print(1)
else:
    print(dynamic_programming(N))