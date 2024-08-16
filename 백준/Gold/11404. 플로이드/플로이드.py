from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N = int(input())
M = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

### 연결 관계 저장
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    graph[k][k] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in range(1, N + 1):
    for col in range(1, N + 1):
        cost = graph[row][col]
        
        if cost == INF:
            print(0, end=" ")
        else:
            print(cost, end=" ")
            
    print()