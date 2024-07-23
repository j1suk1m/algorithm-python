from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y, 0)])
    graph[x][y] = 1 ### 방문 처리
    
    while queue:
        x, y, distance = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if not (0 <= nx and nx < n and 0 <= ny and ny < m):
                continue
            
            next = graph[nx][ny]
            
            if (next == 1): ### 장애물
                continue
            elif (next > 1): ### 음식 발견
                return distance + 1
            else: ### 빈 복도
                queue.append((nx, ny, distance + 1))
                graph[nx][ny] = 1 ### 방문 처리
    
    return 0 ### 아무 음식도 먹을 수 없는 경우
        
n, m = map(int, stdin.readline().rstrip().split())
graph = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(n): 
    graph.append(list(map(int, list(stdin.readline().rstrip()))))
    
for x in range(n):
    for y in range(m):
        if graph[x][y] == 2: ### 윌리암슨수액빨이딱따구리 식구의 위치
            result = bfs(x, y)
            break
        
if (result):
    print("TAK")
    print(result)
else:
    print("NIE")