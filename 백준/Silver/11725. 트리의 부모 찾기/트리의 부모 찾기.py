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
                visited[next] = current ### 방문 처리 시 부모 노드를 저장

N = int(stdin.readline().rstrip())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    node1, node2 = map(int, stdin.readline().rstrip().split())
    
    graph[node1].append(node2)
    graph[node2].append(node1)
    
bfs(1)
print("\n".join(list(map(str, visited[2:]))))