from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(start: int):
    queue = deque([(start)])
    visited[start] = 1
    
    while queue:
        current = queue.popleft()
        jump = A[current]
        
        for next in [current + jump, current - jump]:
            if not (0 < next <= N):
                continue
            elif not visited[next]:
                visited[next] = 1
                queue.append(next)

N = int(input())
A = [0] + list(map(int, input().split()))
S = int(input())
visited = [0] * (N + 1)

### 너비 우선 탐색 알고리즘 실행
bfs(S)

print(sum(visited))