from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
M = int(input())
graph = [[0] * (N + 1) for _ in range(N + 1)]

### 연결 관계 저장
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1 ### a의 무게 > b의 무게
    
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    graph[k][k] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and graph[i][k] and graph[k][j]:
                graph[i][j] = 1
                
for k in range(1, N + 1):
    print(N - sum(graph[k]) - sum(graph[i][k] for i in range(1, N + 1)) - 1)