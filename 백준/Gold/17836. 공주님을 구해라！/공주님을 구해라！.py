from sys import stdin
from collections import deque

### 너비 우선 탐색 알고리즘
def bfs(start_x, start_y, end_x, end_y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    graph[start_x][start_y] = 1 ### 방문 처리
    queue = deque([(start_x, start_y, 0)])
    gram_hour = 10001 ### 그람을 사용했을 때 걸리는 시간
    
    while queue:
        x, y, hour = queue.popleft()
        optimal_hour = min(hour, gram_hour)
        
        if optimal_hour > T:
            return "Fail"
        elif x == end_x and y == end_y:
            return optimal_hour
        else:
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy
                
                if not (1 <= nx <= N and 1 <= ny <= M):
                    continue
                elif graph[nx][ny] == 1: ### 벽
                    continue
                elif graph[nx][ny] == 2: ### 그람
                    graph[nx][ny] = 1 ### 방문 처리
                    gram_hour = hour + 1 + (end_x - nx) + (end_y - ny)
                else: ### 빈 공간
                    graph[nx][ny] = 1
                    queue.append((nx, ny, hour + 1))
                    
    return "Fail" if gram_hour > T else gram_hour
            
input = lambda: stdin.readline().rstrip()

N, M, T = map(int, input().split())
graph = [[0 for _ in range(M + 1)]]

for _ in range(N):
    graph.append([0] + list(map(int, input().split())))
    
print(bfs(1, 1, N, M))