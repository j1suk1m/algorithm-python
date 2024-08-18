from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
answer = [0] * (N + 1) 
indegree = [0] * (N + 1)
queue = deque()

### 연결 관계 저장
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

### 위상 정렬 알고리즘
for node in range(1, N + 1):
    if indegree[node] == 0:
        queue.append((node, 1))
        
while queue:
    current, order = queue.popleft()
    answer[current] = order
    
    for next in graph[current]:
        indegree[next] -= 1
        
        if indegree[next] == 0:
            queue.append((next, order + 1))

print(*answer[1:])