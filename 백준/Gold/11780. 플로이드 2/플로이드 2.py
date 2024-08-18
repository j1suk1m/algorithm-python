from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
path = [[[row] for _ in range(N + 1)] for row in range(N + 1)]

### 연결 관계 저장 
for _ in range(M):
    a, b, c = map(int, input().split())
    
    if c < graph[a][b]:
        graph[a][b] = c

### 플로이드 워셜 알고리즘        
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j or j == k or k == i:
                continue
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + path[k][j]

### 최소 비용 출력
for start in range(1, N + 1):
    for end in range(1, N + 1):
        if graph[start][end] == INF:
            print(0, end=" ")
        else:
            print(graph[start][end], end=" ")   
            
    print()

### 경로 출력               
for start in range(1, N + 1):
    for end in range(1, N + 1):
        if graph[start][end] == INF:
            print(0)
        else:
            print(len(path[start][end]) + 1, *path[start][end], end)