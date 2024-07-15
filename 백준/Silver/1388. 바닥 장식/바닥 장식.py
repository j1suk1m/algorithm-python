from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(x, y):
    current = graph[x][y]
    
    if current == '*':
        return 0
    else: 
        graph[x][y] = '*' ### 방문 표시

        if current == '-':
            y += 1
        else:
            x += 1

        if (0 <= x and x < N and 0 <= y and y < M and graph[x][y] == current):
            dfs(x, y)
        
        return 1

N, M = map(int, stdin.readline().rstrip().split())
graph = []
result = 0

for _ in range(N):
    graph.append(list(stdin.readline().rstrip()))
        
for i in range(N):
    for j in range(M):
        result += dfs(i, j)
            
print(result)