from sys import stdin
from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = True
    count = 0
    
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if not visited[next]:
                count += 1
                queue.append(next)
                visited[next] = True
                
    return count
    
num_of_computers = int(stdin.readline().rstrip())
num_of_pairs = int(stdin.readline().rstrip())
graph = [[] for _ in range(num_of_computers + 1)]
visited = [False] * (num_of_computers + 1)

for _ in range(num_of_pairs):
    computer1, computer2 = map(int, stdin.readline().rstrip().split())
    
    graph[computer1].append(computer2)
    graph[computer2].append(computer1)
    
print(bfs(1))