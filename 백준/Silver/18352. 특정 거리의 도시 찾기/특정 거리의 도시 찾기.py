from sys import stdin
from collections import deque

def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = True
    result = []
    
    while queue:
        node, distance = queue.popleft()

        if distance == K:
            result.append(node)
        else:
            for next in graph[node]:
                if not visited[next]:
                    queue.append((next, distance + 1))
                    visited[next] = True
                
    return result
        
N, M, K, X = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    A, B = map(int, stdin.readline().rstrip().split())
    graph[A].append(B)
    
result = bfs(X)

if len(result) == 0:
    print("-1")
else:
    result.sort()

    for node in result:
        print(node)