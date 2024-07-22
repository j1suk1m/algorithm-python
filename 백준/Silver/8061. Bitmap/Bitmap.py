from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y, 0)])
    answer[x][y] = 0
    
    while queue:
        x, y, distance = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0):
                if answer[nx][ny] > distance + 1:
                    queue.append((nx, ny, distance + 1))
                    answer[nx][ny] = distance + 1
       
n, m = map(int, stdin.readline().rstrip().split())
graph = []
answer = [[n + m - 2] * m for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, list(stdin.readline().rstrip()))))
        
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            bfs(x, y)
            
for row in answer:
    for column in row:
        print(column, end=" ")
    print()