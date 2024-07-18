from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0 ### 방문 처리
    size = 0 ### 음식물의 크기
    
    while queue:
        x, y = queue.popleft()
        size += 1
        
        for dx, dy in zip(dxs, dys): ### 인접한 칸 확인
            nx = x + dx
            ny = y + dy
            
            if 1 <= nx and nx <= N and 1 <= ny and ny <= M and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0 ### 방문 처리
                
    return size

N, M, K = map(int, stdin.readline().rstrip().split())
graph = [[0] * (M + 1) for _ in range(N + 1)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
maximum = 0

for _ in range(K):
    row, column = map(int, stdin.readline().rstrip().split())
    graph[row][column] = 1
    
for x in range(1, N + 1):
    for y in range(1, M + 1):
        if graph[x][y] == 1:
            size = bfs(x, y)
            maximum = size if size > maximum else maximum

print(maximum)