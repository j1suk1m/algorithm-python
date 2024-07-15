from sys import stdin
from collections import deque

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(x, y, 1)])
    graph[x][y] = 0
    
    while queue:
        x, y, count = queue.popleft()
        
        if x == N and y == M:
            return count
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 < nx and nx <= N and 0 < ny and ny <= M and graph[nx][ny] == 1):
                queue.append((nx, ny, count + 1))
                graph[nx][ny] = 0
                
N, M = map(int, stdin.readline().rstrip().split())
graph = [[0] * M]

for _ in range(N):
    graph.append([0] + list(map(int, list(stdin.readline().rstrip()))))   
    
print(bfs(1, 1))