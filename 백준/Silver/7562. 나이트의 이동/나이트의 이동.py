from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y, 0)]) ### 행 좌표, 열 좌표, 전체 이동 횟수
    graph[x][y] = 1 ### 방문 처리
    
    while queue:
        x, y, order = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (nx == target_x and ny == target_y): ### 목적지에 도달한 경우
                return order + 1
            elif (0 <= nx and nx < l and 0 <= ny and ny < l and graph[nx][ny] == 0):
                queue.append((nx, ny, order + 1))
                graph[nx][ny] = 1
            
num_of_test_cases = int(stdin.readline().rstrip())
dxs = [1, 2, 2, 1, -1, -2, -2, -1]
dys = [-2, -1, 1, 2, -2, -1, 1, 2]

for _ in range(num_of_test_cases):
    l = int(stdin.readline().rstrip())
    x, y = map(int, stdin.readline().rstrip().split())
    target_x, target_y = map(int, stdin.readline().rstrip().split())
    graph = [[0] * l for _ in range(l)]
    
    print(bfs(x, y) if (x != target_x or y != target_y) else 0)
    