from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 4)

def dfs(x, y):
    area = 0
    graph[x][y] = 0
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        
        if (0 <= nx and nx < N and 0 <= ny and ny < N and graph[nx][ny] == 1):
            area += dfs(nx, ny)
            
    return 1 + area
    
N = int(stdin.readline().rstrip())
graph = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
houses = []
count = 0

for _ in range(N):
    graph.append(list(map(int, list(stdin.readline().rstrip()))))
                        
for x in range(N):
    for y in range(N):
        if graph[x][y] == 1:
            houses.append(dfs(x, y))
            count += 1

houses.sort()
            
print(count)
print("\n".join(list(map(str, houses))))