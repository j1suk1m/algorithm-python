from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(start) -> list:
    visited[start] = 1
    queue = deque([(start, 0)])
    answer = [0, 0, 0]
    
    while queue:
        current, distance = queue.popleft()
        
        if distance > answer[1]:
            answer = [current, distance, 1]
        elif distance == answer[1]:
            if current < answer[0]:
                answer[0] = current
            
            answer[2] += 1
        
        for next in graph[current]:
            if not visited[next]:
                visited[next] = 1
                queue.append((next, distance + 1))
        
    return answer

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]            
visited = [0] * (N + 1)
start = 1

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
print(*bfs(start))