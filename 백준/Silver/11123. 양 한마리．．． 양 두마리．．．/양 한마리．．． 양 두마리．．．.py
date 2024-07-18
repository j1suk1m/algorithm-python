from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5)

def dfs(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    graph[x][y] = '.'
    
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy
        
        if (0 <= nx and nx < H and 0 <= ny and ny < W and graph[nx][ny] == '#'):
            dfs(nx, ny)
            
    return 1
    
T = int(stdin.readline().rstrip())

for _ in range(T):
    H, W = map(int, stdin.readline().rstrip().split())
    graph = []
    result = 0
    
    for _ in range(H):
        graph.append(list(stdin.readline().rstrip()))
        
    for x in range(H):
        for y in range(W):
            if graph[x][y] == '#':
                result += dfs(x, y)
                
    print(result)