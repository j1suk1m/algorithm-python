from sys import stdin
from collections import deque

def bfs(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    queue = deque([(x, y, 0)])
    graph[x][y] = -1
    
    while queue:
        x, y, depth = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx and nx < row and 0 <= ny and ny < column):
                next = graph[nx][ny]
                
                if next == -1:
                    continue
                elif next == 0:
                    queue.append((nx, ny, depth + 1))
                    graph[nx][ny] = -1
                else: ### 1이 적혀 있는 칸에 도착한 경우
                    return depth + 1
                
    return -1
    
row, column = 5, 5
graph = []

for _ in range(column):
    graph.append(list(map(int, stdin.readline().rstrip().split())))

r, c = map(int, stdin.readline().rstrip().split())

print(bfs(r, c))