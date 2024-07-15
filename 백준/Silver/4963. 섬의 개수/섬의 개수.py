from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(x, y):
    graph[x][y] = 0
    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx and nx < h and 0 <= ny and ny < w and graph[nx][ny] == 1):
            dfs(nx, ny)
            
    return 1
    
dx = [-1, 1, 0, 0, -1, -1, 1, 1] ### 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하
dy = [0, 0, -1, 1, -1, 1, -1, 1] ### 상, 하, 좌, 우, 좌상, 우상, 좌하, 우하

while True:
    w, h = map(int, stdin.readline().rstrip().split())
    
    if w == 0 and h == 0:
        break
    
    graph = []
    result = 0
    
    for _ in range(h):
        graph.append(list(map(int, stdin.readline().rstrip().split())))
        
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                result += dfs(i, j)
                
    print(result)