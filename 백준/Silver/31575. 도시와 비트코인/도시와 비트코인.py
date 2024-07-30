from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0 ### 방문 처리
    isPossible = False
    
    while queue:
        x, y = queue.popleft()
        
        if x == M - 1 and y == N - 1:
            isPossible = True
            break
        
        for dx, dy in [(1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1):
                queue.append((nx, ny))
                graph[nx][ny] = 0 ### 방문 처리
            
    return isPossible

N, M = map(int, stdin.readline().rstrip().split())
graph = [list(map(int, stdin.readline().rstrip().split())) for _ in range(M)]

if bfs(0, 0):
    print("Yes")
else:
    print("No")