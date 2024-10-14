from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(x: int, y: int):
    graph[x][y] = 0
    queue = deque([(x, y)])
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if graph[nx][ny] == 255:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                
    return 1
        
N, M = map(int, input().split())
RGB = list(list(map(int, input().split())) for _ in range(N))
graph = list(list(0 for _ in range(M)) for _ in range(N))
T = int(input())
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
answer = 0

for row in range(N):
    for col in range(M):
        pixels = sum(RGB[row][3 * col:3 * col + 3])
        
        if pixels >= 3 * T:
            graph[row][col] = 255
            
for row in range(N):
    for col in range(M):
        if graph[row][col] == 255:
            answer += bfs(row, col)
            
print(answer)