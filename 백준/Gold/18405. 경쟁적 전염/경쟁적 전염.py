from sys import stdin
from collections import deque
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs():
    while queue:
        x, y, second = queue.popleft()
        current_virus = graph[x][y]
        
        if second >= S:
            break
        
        ### 상하좌우 탐색
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            ### 범위를 벗어나는 경우
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            elif graph[nx][ny] == 0:
                graph[nx][ny] = current_virus
                queue.append((nx, ny, second + 1))
                
N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
initial_virus = []
queue = deque()

### 초기 상태의 바이러스 좌표를 우선순위 큐에 저장
for x in range(N):
    for y in range(N):
        virus = graph[x][y]
        
        if virus > 0:
            heappush(initial_virus, (virus, x, y))

### 바이러스 번호가 작은 순으로 바이러스 좌표를 큐에 저장          
while initial_virus:
    virus, x, y = heappop(initial_virus)
    queue.append((x, y, 0))
            
### 너비 우선 탐색 실행
bfs()
    
print(graph[X - 1][Y - 1])