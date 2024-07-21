from sys import stdin
from collections import deque
from copy import deepcopy

def bfs(x, y):
    queue = deque([(x, y)])
    graph_copy[x][y] = 1 
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx and nx < N and 0 <= ny and ny < M and graph_copy[nx][ny] == 0):
                queue.append((nx, ny))
                graph_copy[nx][ny] = 1
                
N, M = map(int, stdin.readline().rstrip().split())
graph = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(map(int, stdin.readline().rstrip().split())))
    
maximum_area = 0

for i in range(N * M):
    for j in range(N * M):
        for k in range(N * M):
            if (i == j or j == k or k == i):
                continue
            
            first_wall_x, first_wall_y = i // M, i % M
            second_wall_x, second_wall_y = j // M, j % M
            third_wall_x, third_wall_y = k // M, k % M

            if (graph[first_wall_x][first_wall_y] != 0 or graph[second_wall_x][second_wall_y] != 0 or graph[third_wall_x][third_wall_y] != 0):
                continue
            
            graph_copy = deepcopy(graph)
            
            graph_copy[first_wall_x][first_wall_y] = 1
            graph_copy[second_wall_x][second_wall_y] = 1
            graph_copy[third_wall_x][third_wall_y] = 1
            
            for x in range(N):
                for y in range(M):
                    if graph_copy[x][y] == 2:
                        bfs(x, y)
            
            result = sum(row.count(0) for row in graph_copy)
            
            if result > maximum_area:
                maximum_area = result

print(maximum_area)  