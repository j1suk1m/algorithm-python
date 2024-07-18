from sys import stdin
from collections import deque

def bfs(node):
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        current_degree = counted[current]

        for next in graph[current]:
            if counted[next] == 0 and next != node:
                queue.append(next)
                counted[next] += (current_degree + 1)
                
    return sum(counted)

N, M = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
minimum = N * N
answer = 1

for _ in range(M):
    A, B = map(int, stdin.readline().rstrip().split())
    
    graph[A].append(B)
    graph[B].append(A)
    
for node in range(1, N + 1):
    counted = [0] * (N + 1)
    search_result = bfs(node)

    if search_result < minimum:
        answer = node
        minimum = search_result
    
print(answer)