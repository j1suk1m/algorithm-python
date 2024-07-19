from sys import stdin
from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = 1
    
    while queue:
        current = queue.popleft()
        
        for next in graph[current]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1
                
    return 1

N, M = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
result = 0

for _ in range(M):
    u, v = map(int, stdin.readline().rstrip().split())
    
    graph[u].append(v)
    graph[v].append(u)
    
for node in range(1, N + 1):
    if visited[node] == 0:
        result += bfs(node)
        
print(result)