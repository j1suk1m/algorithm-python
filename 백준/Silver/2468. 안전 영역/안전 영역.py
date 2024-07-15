from sys import stdin, setrecursionlimit
from copy import deepcopy

setrecursionlimit(10 ** 6)

def dfs(x, y, height):
    graph_copy[x][y] = height
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx and nx < N and 0 <= ny and ny < N and graph_copy[nx][ny] > height):
            dfs(nx, ny, height)
    
    return 1

N = int(stdin.readline().rstrip())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
current_height = 0
maximum_count = -1

for _ in range(N):
    graph.append(list(map(int, stdin.readline().rstrip().split())))

while True:
    graph_copy = deepcopy(graph)
    search_result = 0
    
    for x in range(N):
        for y in range(N):
            if graph_copy[x][y] > current_height:
                search_result += dfs(x, y, current_height)
                
    if search_result == 0:
        print(maximum_count)
        break
    elif search_result > maximum_count:
        maximum_count = search_result
        
    current_height += 1