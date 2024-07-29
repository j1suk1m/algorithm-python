from sys import stdin
from collections import deque

def bfs(x, y, updated_data):
    queue = deque([(x, y)])
    original_data = before_graph[x][y]
    before_graph[x][y] = updated_data ### 방문 처리
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx < N and 0 <= ny < M and before_graph[nx][ny] == original_data):
                queue.append((nx, ny))
                before_graph[nx][ny] = updated_data ### 방문 처리
    
N, M = map(int, stdin.readline().rstrip().split())
before_graph = [] ### 백신 접종 전 그래프
after_graph = [] ### 백신 접종 후 그래프 
isInjected = False ### 백신 접종 완료 여부

for _ in range(N):
    before_graph.append(list(map(int, stdin.readline().rstrip().split())))
    
for _ in range(N):
    after_graph.append(list(map(int, stdin.readline().rstrip().split())))
    
for x in range(N):
    for y in range(M):
        if before_graph[x][y] != after_graph[x][y]:
            bfs(x, y, after_graph[x][y])
            isInjected = True
            break
        
    if isInjected:
        break
     
if before_graph == after_graph:
    print("YES")
else:
    print("NO")