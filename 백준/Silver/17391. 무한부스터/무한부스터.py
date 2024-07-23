from sys import stdin
from collections import deque

def bfs(x, y):
    item = graph[x][y]
    queue = deque([(x, y, item, 0)])
    graph[x][y] = 0 ### 방문 처리
    
    while queue:
        x, y, item, depth = queue.popleft()
        
        if (x == N - 1 and y == M - 1): ### 도착 지점에 도달한 경우
            return depth
        
        for dx in range(1, item + 1): ### 아래쪽으로 이동
            nx = x + dx
            
            if (0 <= nx < N and graph[nx][y] > 0):
                queue.append((nx, y, graph[nx][y], depth + 1))
                graph[nx][y] = 0 ### 방문 처리
        
        for dy in range(1, item + 1): ### 오른쪽으로 이동
            ny = y + dy
            
            if (0 <= ny < M and graph[x][ny] > 0):
                queue.append((x, ny, graph[x][ny], depth + 1))
                graph[x][ny] = 0 ### 방문 처리
    
N, M = map(int, stdin.readline().rstrip().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, stdin.readline().rstrip().split())))
    
print(bfs(0, 0))