from sys import stdin
from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    current = graph[x][y]
    graph[x][y] = '*' ### 방문 표시
    count = 0 ### 병사의 수
    
    while queue:
        x, y = queue.popleft()
        count += 1
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx and nx < M and 0 <= ny and ny < N and graph[nx][ny] == current):
                queue.append((nx, ny))
                current = graph[nx][ny] ### 아군만 집계하기 위한 변수
                graph[nx][ny] = '*'
                
    idx = 0 if current == 'W' else 1
    answers[idx] += (count ** 2) ### 병사의 수의 제곱이 위력
    
N, M = map(int, stdin.readline().rstrip().split())
graph = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
answers = [0, 0] ### 아군의 위력의 합, 적국의 위력의 합

for _ in range(M):
    graph.append(list(stdin.readline().rstrip()))
    
for x in range(M):
    for y in range(N):
        if graph[x][y] != '*':
            bfs(x, y)
            
print(" ".join(list(map(str, answers))))