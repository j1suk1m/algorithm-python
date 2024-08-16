from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[INF] * (N + 1) for _ in range(N + 1)]
answer = 0

### 연결 관계 저장
for _ in range(R):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l
    
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    graph[k][k] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

### 획득 가능한 아이템 개수 계산                
for zone in range(1, N + 1):
    item = sum([items[other] for other in range(1, N + 1) if graph[zone][other] <= M])
    
    if answer < item:
        answer = item
        
print(answer)