from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y, 0)])
    graph[x][y] = 1 ### 방문 표시
    
    while queue:
        x, y, move = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (1 <= nx <= N and 1 <= ny <= N and graph[nx][ny] == 0):
                queue.append((nx, ny, move + 1))    
                graph[nx][ny] = move + 1 ### 방문 표시
        
N, M = map(int, stdin.readline().rstrip().split())
X, Y = map(int, stdin.readline().rstrip().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
target = [] ### 상대편 말의 (x, y) 좌표 튜플 리스트
dxs = [-2, -2, -1, -1, 1, 1, 2, 2]
dys = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(M):
    A, B = map(int, stdin.readline().rstrip().split())
    target.append((A, B))
    
bfs(X, Y)

for x, y in target:
    print(graph[x][y], end=" ")