from sys import stdin

N = int(stdin.readline().rstrip())
A = [0] + list(map(int, stdin.readline().rstrip().split()))

if N == 1:
    print(A[1])
else:
    dp = [number for number in A]
    
    for current in range(1, N + 1):
        for rest in range(1, current + 1):
            if A[current] > A[rest]:
                dp[current] = max(dp[current], dp[rest] + A[current]) 
    
    print(max(dp))