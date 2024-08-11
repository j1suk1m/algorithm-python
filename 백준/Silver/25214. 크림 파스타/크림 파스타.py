from sys import stdin

def dynamic_programming(N: int, A: list) -> list:
    dp = [0] * (N)
    minimum = A[0]
    
    for number in range(1, N):
        if A[number] < minimum: ### 배열의 최솟값 저장
            minimum = A[number] 
        
        dp[number] = max(A[number] - minimum, dp[number - 1])
        
    return dp
    
N = int(stdin.readline().rstrip())
A = list(map(int, stdin.readline().rstrip().split()))

print(*dynamic_programming(N, A))