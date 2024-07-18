from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0
    area = 0
    
    while queue:
        x, y = queue.popleft()
        area += 1
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx and nx < n and 0 <= ny and ny < m and graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                
    return area

n, m = map(int, stdin.readline().rstrip().split())
graph = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
num_of_painting = 0
maximum_area = 0

for _ in range(n):
    graph.append(list(map(int, stdin.readline().rstrip().split())))
    
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            area = bfs(x, y)
            maximum_area = area if area > maximum_area else maximum_area
            num_of_painting += 1

print(num_of_painting)
print(maximum_area)