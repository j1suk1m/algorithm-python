from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()

### 깊이 우선 탐색 알고리즘
def dfs(node: int, depth: int):
    global order
    
    visited[node] = 1
    node_values[node] = depth * order
    order += 1
    
    for next in graph[node]:
        if visited[next] == 0: 
            dfs(next, depth + 1)
    
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
node_values = [0] * (N + 1)
order = 1

### 인접 정점 정보 저장
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
### 인접 정점을 내림차순으로 방문하기 위한 정렬
for edge in graph:
    edge.sort(reverse=True)
    
### 깊이 우선 탐색
dfs(R, 0)

print(sum(node_values))