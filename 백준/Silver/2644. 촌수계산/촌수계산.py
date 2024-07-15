from sys import stdin
from collections import deque

def bfs(node):
    queue = deque([(node, 0)])
    visited[node] = True
    
    while queue:
        node, degree = queue.popleft()
        
        if node == end_node:
            return degree
        
        for next in graph[node]:
            if not visited[next]:
                queue.append((next, degree + 1))
                visited[next] = True
                
    return -1    

n = int(stdin.readline().rstrip())
start_node, end_node = map(int, stdin.readline().rstrip().split())
m = int(stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    x, y = map(int, stdin.readline().rstrip().split()) ### x는 y의 부모
    
    graph[x].append(y)
    graph[y].append(x)

print(bfs(start_node))