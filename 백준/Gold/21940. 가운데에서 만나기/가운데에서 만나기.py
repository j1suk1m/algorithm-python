from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
candidates = []

### 연결 관계 저장
for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A][B] = T
    
K = int(input())
friends = list(map(int, input().split()))
    
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    graph[k][k] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
### (최대 왕복 시간, 도시 번호) 튜플 저장
for city in range(1, N + 1):
    maximum_time = 0
    
    for friend in friends:
        if graph[friend][city] != INF and graph[city][friend] != INF:
            maximum_time = max(maximum_time, graph[friend][city] + graph[city][friend])
        
    candidates.append((maximum_time, city))
    
candidates = sorted(candidates, key=lambda x: (x[0], x[1]))
minimum_time = candidates[0][0]

for candidate in candidates:
    if candidate[0] == minimum_time:
        print(candidate[1], end=" ")