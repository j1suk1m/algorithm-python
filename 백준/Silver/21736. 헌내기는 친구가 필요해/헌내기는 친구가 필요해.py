from sys import stdin
from collections import deque

def bfs(x, y):
    count = 0
    queue = deque([(x, y)])
    graph[x][y] = 'X'
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx < N and 0 <= ny < M):
                if graph[nx][ny] == 'P':
                    count += 1
                    queue.append((nx, ny))
                    graph[nx][ny] = 'X'
                elif graph[nx][ny] == 'O':
                    queue.append((nx, ny))
                    graph[nx][ny] = 'X'
                    
    return count
        
N, M = map(int, stdin.readline().rstrip().split())
graph = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(stdin.readline().rstrip()))
    
for x in range(N):
    for y in range(M):
        if graph[x][y] == 'I':
            result = bfs(x, y)
            
if result:
    print(result)
else:
    print("TT")