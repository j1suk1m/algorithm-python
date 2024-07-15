from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(x, y):
    if graph[x][y] == 1: ### 배추가 있는 땅
        graph[x][y] = 0 ### 방문 표시
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if (0 <= nx and nx < N and 0 <= ny and ny < M and graph[nx][ny] == 1):
                dfs(nx, ny) ### 상, 하, 좌, 우 방문
        
        return 1
            
    return 0

T = int(stdin.readline().rstrip())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    M, N, K = map(int, stdin.readline().rstrip().split())
    graph = [[0] * M for _ in range(N)]
    result = 0

    for _ in range(K):
        X, Y = map(int, stdin.readline().rstrip().split())
        graph[Y][X] = 1 ### 배추가 있는 땅 표시
        
    for i in range(N):
        for j in range(M):
            result += dfs(i, j)
            
    print(result)