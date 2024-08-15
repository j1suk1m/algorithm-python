from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]
isSolved = False

### 연결 관계 저장
for i in range(1, N):
    M = int(input())
    C = list(map(int, input().split()))
    
    for c in C:
        graph[i][c] = 1
        
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if (not graph[i][j]) and graph[i][k] and graph[k][j]:
                graph[i][j] = 1

### 싸이클 존재 여부 판별
for i in range(1, N + 1):
    if graph[1][i] and graph[i][i]:
        print("CYCLE")
        isSolved = True
        break
    
if not isSolved:
    print("NO CYCLE")