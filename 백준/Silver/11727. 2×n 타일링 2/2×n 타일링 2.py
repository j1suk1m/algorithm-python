from sys import stdin

def dynamic_programming(n: int) -> int:
    dp = [0] * (n + 1)
    
    dp[1] = 1
    dp[2] = 3
    
    for number in range(3, n + 1):
        dp[number] = dp[number - 1] + 2 * dp[number - 2]
        
    return dp[n] % 10007
    
n = int(stdin.readline().rstrip())

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    print(dynamic_programming(n))