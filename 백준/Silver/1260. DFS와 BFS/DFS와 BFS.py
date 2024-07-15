from sys import stdin
from collections import deque

def dfs(node):
    visited[node] = True
    print(node, end=" ")
    
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
            
def bfs(node):
    queue = deque([node])
    visited[node] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
            
            
N, M, V = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    node1, node2 = map(int, stdin.readline().rstrip().split())
    
    graph[node1].append(node2)
    graph[node2].append(node1)
    
for connections in graph:
    connections.sort()
        
visited = [False] * (N + 1)
dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)