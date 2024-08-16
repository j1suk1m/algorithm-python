from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
candidates = []

### 연결 관계 저장
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A][B] = C
    graph[B][A] = C
    
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j and j != k and k != i:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for computer in range(1, N + 1):
    average_time = sum([graph[computer][rest] for rest in range(1, N + 1) if computer != rest]) / (N - 1)
    candidates.append((average_time, computer))
    
candidates = sorted(candidates, key=lambda x: (x[0], x[1]))
print(candidates[0][1])