from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(start: int, end: int):
    queue = deque([(start, 0)])
    visited[start] = 1
    
    while queue:
        current, count = queue.popleft()
        
        if current == end:
            return count
    
        for next in (current + U, current - D):
            if not (0 < next <= F):
                continue
            elif not visited[next]:
                visited[next] = 1
                queue.append((next, count + 1))
                
    return -1

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)

### 너비 우선 탐색 알고리즘 실행
answer = bfs(S, G)

if answer == -1:
    print("use the stairs")
else:
    print(answer)