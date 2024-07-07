from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
A = []
result = []

for _ in range(N):
    A.append(list(map(int, stdin.readline().rstrip().split())))
    
for i in range(N):
    result.append([x + y for x, y in zip(A[i], list(map(int, stdin.readline().rstrip().split())))])
    
for i in range(N):
    for j in range(M):
        print(result[i][j], end=" ")
    print()