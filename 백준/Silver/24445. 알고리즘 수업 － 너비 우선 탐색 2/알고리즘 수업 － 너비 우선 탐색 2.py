from sys import stdin
from collections import deque

def bfs(node):
    visited[node] = order = 1
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        
        for next in graph[current]:
            if not visited[next]:
                order += 1
                visited[next] = order ### 방문 처리 + 방문 순서
                queue.append(next)

N, M, R = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, stdin.readline().rstrip().split())
    
    graph[u].append(v)
    graph[v].append(u)

### 인접 정점을 내림차순으로 방문하기 위한 정렬
for edge in graph:
    edge.sort(reverse=True)
    
bfs(R)
print("\n".join(list(map(str, visited[1:]))))