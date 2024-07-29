from sys import stdin
from collections import deque
    
def bfs(x, y):
    start = graph[x][y]
    sheep = 1 if start == 'k' else 0 ### 현재 영역의 양의 수
    wolf = 1 if start == 'v' else 0 ### 현재 영역의 늑대의 수
    queue = deque([(x, y)])
    graph[x][y] = '#' ### 방문 처리
    
    while queue:
        x, y = queue.popleft()
    
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
        
            if (0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#'):
                if graph[nx][ny] == 'k':
                    sheep += 1
                elif graph[nx][ny] == 'v':
                    wolf += 1
                    
                queue.append((nx, ny))
                graph[nx][ny] = '#' ### 방문 처리
                
    return (sheep, wolf)
    
R, C = map(int, stdin.readline().rstrip().split())
graph = []
total_sheep = 0 
total_wolf = 0

for _ in range(R):
    graph.append(list(stdin.readline().rstrip()))

for x in range(R):
    for y in range(C):
        if graph[x][y] != '#':
            sheep, wolf = bfs(x, y)
            
            if sheep == 0 and wolf == 0:
                continue
            elif sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
                
print(total_sheep, total_wolf)