from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)

def dfs(x, y):
    global sheep, wolf
    
    if graph[x][y] == 'o':
        sheep += 1 ### 현재 영역의 양의 수
    elif graph[x][y] == 'v':
        wolf += 1 ### 현재 영역의 늑대의 수
        
    graph[x][y] = '#' ### 방문 처리
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        
        if (0 <= nx < R and 0 <= ny < C and graph[nx][ny] != '#'):
            dfs(nx, ny)
            
    return (sheep, wolf)
    
R, C = map(int, stdin.readline().rstrip().split())
graph = []
total_sheep = 0 
total_wolf = 0

for _ in range(R):
    graph.append(list(stdin.readline().rstrip()))

for x in range(R):
    for y in range(C):
        if graph[x][y] != '#':
            sheep, wolf = 0, 0
            sheep, wolf = dfs(x, y)
            
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
                
print(total_sheep, total_wolf)