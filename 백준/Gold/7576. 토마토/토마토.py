from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs():    
    while queue:
        x, y, date = queue.popleft()
        
        ### 상하좌우 탐색
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            ### 격자를 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = date + 1
                queue.append((nx, ny, date + 1))

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
queue = deque()
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
is_ripen = True ### 모든 토마토가 익었는지 확인
date = 0

### 익은 토마토가 있는 칸의 좌표를 큐에 저장
for x in range(N):
    for y in range(M):
        if graph[x][y] == 1:
            queue.append((x, y, 1))

### 너비 우선 탐색 실행            
bfs()
            
for x in range(N):
    if not is_ripen:
        break
    
    for y in range(M):
        ### 익지 않은 토마토가 남아 있는 경우
        if graph[x][y] == 0:
            date = -1
            is_ripen = False
            break
        elif graph[x][y] == -1:
            continue
        else:
            date = max(date, graph[x][y])
            
print(date) if date == -1 else print(date - 1)