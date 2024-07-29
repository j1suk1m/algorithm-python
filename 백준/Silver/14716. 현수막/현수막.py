from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)

def dfs(x, y):
    graph[x][y] = 0 ### 방문 처리
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        
        if (0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1):
            dfs(nx, ny)
    
    return 1
    
M, N = map(int, stdin.readline().rstrip().split())
graph = []
dxs = [-1, 1, 0, 0, -1, -1, 1, 1] ### 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dys = [0, 0, -1, 1, -1, 1, -1, 1] ### 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
result = 0

for _ in range(M):
    graph.append(list(map(int, stdin.readline().rstrip().split())))
    
for x in range(M):
    for y in range(N):
        if graph[x][y] == 1:
            result += dfs(x, y)
            
print(result)