from sys import stdin

def dynamic_programming(N: int) -> int:
    dp = [0] * (N + 1) 
    
    dp[1] = 1
    dp[2] = 1

    for number in range(3, N + 1):
        ### 마지막 숫자가 0일 경우 N - 1자리 이친수의 개수와 동일
        ### 마지막 숫자가 1일 경우 그 앞 숫자는 0으로 고정되므로 N - 2자리 이친수의 개수와 동일
        dp[number] = dp[number - 1] + dp[number - 2] 
        
    return dp[N]

N = int(stdin.readline().rstrip())

if N <= 2:
    print(1)
else:
    print(dynamic_programming(N))