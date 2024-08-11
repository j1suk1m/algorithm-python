from sys import stdin

n = int(stdin.readline().rstrip())

if n <= 2:
    print(n)
else:
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 2
    
    for person in range(3, n + 1):
        dp[person] = (dp[person - 1] + dp[person - 2]) % 10
        
    print(dp[n])