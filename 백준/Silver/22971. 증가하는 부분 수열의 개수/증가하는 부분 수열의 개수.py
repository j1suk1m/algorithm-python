from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
MOD = 998244353

if N == 1:
    input()
    print(1)
else:
    A = [0] + list(map(int, input().split()))
    dp = [1 for _ in range(N + 1)] ### 증가하는 부분 수열의 개수 리스트
    
    for current in range(2, N + 1):
        current_number = A[current]
        
        for previous in range(1, current):
            previous_number = A[previous]

            if current_number > previous_number:
                dp[current] += (dp[previous] % MOD)
                
        dp[current] %= MOD

    print(*dp[1:])