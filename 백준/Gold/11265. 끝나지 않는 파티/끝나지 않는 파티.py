from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N, M = map(int, input().split())
graph = [[0] * (N + 1)] + list(([0] + list(map(int, input().split()))) for _ in range(N))

### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(M):
    A, B, C = map(int, input().split())
    
    if graph[A][B] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")