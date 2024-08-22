from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())

if N == 1:
    print(int(input()))
else:
    A = [0] + list(map(int, input().split()))
    dp = [0 for _ in range(N + 1)] ### 부분 수열의 최대 합 리스트
    dp[1] = A[1]
    
    for current in range(2, N + 1):
        current_number = A[current]
        
        for previous in range(1, current):
            previous_number = A[previous]

            if current_number < previous_number:
                dp[current] = max(dp[current], dp[previous] + current_number)
            else:
                dp[current] = max(dp[current], current_number)

    print(max(dp))