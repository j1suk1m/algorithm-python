from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 4)

def dfs(x, y):
    area = 0
    graph[x][y] = 1
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        
        if (0 <= nx and nx < N and 0 <= ny and ny < M and graph[nx][ny] == 0):
            area += dfs(nx, ny)
            
    return 1 + area
    
    

M, N, K = map(int, stdin.readline().rstrip().split())
graph = [[0] * M for _ in range(N)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
area_list = []
count = 0

for _ in range(K):
    left_x, left_y, right_x, right_y = map(int, stdin.readline().rstrip().split())
    
    for x in range(left_x, right_x):
        for y in range(left_y, right_y):
            graph[x][y] = 1
                        
for x in range(N):
    for y in range(M):
        if graph[x][y] == 0:
            area_list.append(dfs(x, y))
            count += 1

area_list.sort()
            
print(count)
print(" ".join(list(map(str, area_list))))