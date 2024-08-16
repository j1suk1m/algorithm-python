from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF] * (V + 1) for _ in range(V + 1)]

### 연결 관계 저장
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
### 플로이드 워셜 알고리즘
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

### 사이클의 도로 길이의 합 저장 후 정렬              
cycle = sorted([graph[k][k] for k in range(1, V + 1)])
answer = cycle[0]

if answer == INF:
    print(-1)
else:
    print(answer)