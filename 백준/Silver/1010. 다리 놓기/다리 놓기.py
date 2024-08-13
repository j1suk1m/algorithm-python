from sys import stdin

max = 29
T = int(stdin.readline().rstrip())
dp = [[0] * (max + 1) for _ in range(max + 1)]
        
for row in range(1, max + 1):
    for col in range(1, max + 1):
        if col == 1: ### nC1 == n
            dp[row][col] = row
        else: ### nCr == n-1Cr + n-1Cr-1 
            dp[row][col] = dp[row - 1][col] + dp[row - 1][col - 1]
            
for _ in range(T):
    N, M = map(int, stdin.readline().rstrip().split())
    
    ### M개 중에 순서 없이 N개를 뽑는 조합의 개수와 동일
    if N == 1:
        print(M)
    else:
        print(dp[M][N])