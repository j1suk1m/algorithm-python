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
            
            if (0 <= nx < n and 0 <= ny < m and answer[nx][ny] == -1):
                queue.append((nx, ny, distance + 1))
                answer[nx][ny] = distance + 1
        
n, m = map(int, stdin.readline().rstrip().split())
graph = []
answer = [[-1] * m for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for row_index in range(n):
    row = list(map(int, stdin.readline().rstrip().split()))
    graph.append(row)
    
    for col_index in range(m):
        number = row[col_index]
        
        if number == 2:
            target_x, target_y = row_index, col_index
        elif number == 0:
            answer[row_index][col_index] = 0
        
bfs(target_x, target_y)

for row in answer:
    for col in row:
        print(col, end=" ")
    print()