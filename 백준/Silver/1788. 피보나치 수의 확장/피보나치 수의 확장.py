from sys import stdin

def extended_fibonacci(n: int) -> int:
    n = abs(n)
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 1
    
    for number in range(3, n + 1):
        dp[number] = (dp[number - 1] + dp[number - 2]) % 1000000000
        
    return dp[n]
    
n = int(stdin.readline().rstrip())

if n == 0:
    print(0)
    print(0)
elif abs(n) <= 2:
    if n == -2:
        print(-1)
    else:
        print(1)
        
    print(1)
else:
    if n < 0 and abs(n) % 2 == 0:
        print(-1)
    else:
        print(1)
        
    print(extended_fibonacci(n))