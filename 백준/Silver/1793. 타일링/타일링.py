from sys import stdin

def dynamic_programming(n: int) -> int:
    dp = [0] * 251 ### 가능한 타일링의 수
    
    dp[1] = 1 ### 2 * 1 타일 1개
    dp[2] = 3 ### 2 * 1 타일 2개, 1 * 2 타일 2개, 2 * 2 타일 1개
    
    for width in range(3, n + 1):
        dp[width] = dp[width - 1] + 2 * dp[width - 2]
        
    return dp[n]

while True:
    n = stdin.readline().rstrip()
    
    if n == "":
        break
    
    n = int(n)
    
    if n <= 1:
        print(1)
    elif n == 2:
        print(3)
    else:
        print(dynamic_programming(n))