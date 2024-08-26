from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N, K = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
is_big_world = False

### 연결 관계 저장
for _ in range(K):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1
    
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j or j == k or k == i:
                continue
            else:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for row in range(1, N):
    for col in range(row + 1, N + 1):
        if graph[row][col] > 6:
            is_big_world = True
            break
        
if is_big_world:
    print("Big World!")
else:
    print("Small World!")