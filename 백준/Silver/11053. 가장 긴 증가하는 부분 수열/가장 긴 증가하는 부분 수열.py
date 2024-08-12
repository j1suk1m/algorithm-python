from sys import stdin

N = int(stdin.readline().rstrip())
A = [0] + list(map(int, stdin.readline().rstrip().split()))

if N == 1:
    print(1)
else:
    dp = [1] * (N + 1) ### dp[idx] == idx를 수열의 최댓값으로 갖는 수열의 길이
    
    for current in range(1, N + 1):
        for rest in range(1, current + 1):
            if A[current] > A[rest]:
                dp[current] = max(dp[current], dp[rest] + 1) 
    
    print(max(dp))