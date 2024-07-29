from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6 * 2)

def dfs(x, y):
    graph[x][y] = 2 ### 방문 처리
    
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        
        if (0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 0):
            dfs(nx, ny)
            
M, N = map(int, stdin.readline().rstrip().split())
graph = []

for _ in range(M):
    graph.append(list(map(int, list(stdin.readline().rstrip()))))

for col in range(N):
    if graph[0][col] == 0: ### 첫번째 행의 흰색 부분에서 탐색 시작
        dfs(0, col)
        
if 2 in graph[M - 1]: ### 마지막 행까지 탐색했는지 확인
    print("YES")
else:
    print("NO")