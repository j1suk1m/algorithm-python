from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    dp = [0] * N
    answer = X[0]
    
    dp[0] = X[0]
    
    for index in range(1, N):
        dp[index] = max(X[index], X[index] + dp[index - 1])
        answer = max(answer, dp[index])
        
    print(answer)