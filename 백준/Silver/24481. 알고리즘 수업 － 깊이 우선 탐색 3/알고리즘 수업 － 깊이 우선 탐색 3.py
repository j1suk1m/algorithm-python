from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)
input = lambda: stdin.readline().rstrip()

### 깊이 우선 탐색 알고리즘
def dfs(node: int, depth: int):
    visited[node] = depth ### 방문 여부와 노드 깊이를 동시에 저장
    
    for next in graph[node]:
        if visited[next] == -1: ### 방문하지 않은 경우
            dfs(next, depth + 1)
    
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [-1] * (N + 1)

### 인접 정점 저장
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
### 인접 정점을 오름차순으로 방문하기 위한 정렬
for edge in graph:
    edge.sort()
    
### 깊이 우선 탐색
dfs(R, 0)

for depth in visited[1:]:
    print(depth)