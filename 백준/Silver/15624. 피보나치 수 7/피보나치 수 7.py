from sys import stdin

n = int(stdin.readline().rstrip())

if n <= 1:
    print(n)
elif n == 2:
    print(1)
else:
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 1
    
    for order in range(3, n + 1):
        dp[order] = (dp[order - 1] + dp[order - 2]) % 1000000007
        
    print(dp[n])