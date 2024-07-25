from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y, 0)])
    graph[x][y] = 1
    
    while queue:
        x, y, depth = queue.popleft()
        
        if (x == N - 1 and y == M - 1):
            return depth
        
        if x % 2:
            dys = dys_of_odd_row
        else:
            dys = dys_of_even_row
            
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0):
                queue.append((nx, ny, depth + 1))
                graph[nx][ny] = 1
                
    return -1
        
N, M, K = map(int, stdin.readline().rstrip().split())
graph = [[0] * M for _ in range(N)]
dxs = [-1, -1, 0, 0, 1, 1]
dys_of_odd_row = [0, 1, -1, 1, 0, 1]
dys_of_even_row = [-1, 0, -1, 1, -1, 0]

for _ in range(K):
    Y, X = map(int, stdin.readline().rstrip().split())
    graph[Y][X] = 1
    
print(bfs(0, 0))