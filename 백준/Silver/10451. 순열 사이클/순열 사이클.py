from sys import stdin

def dfs(number):
    visited[number] = True
    next = graph[number]
    
    if not visited[next]:
        return dfs(next)
    else:
        return next
    
T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    graph = [0] + list(map(int, stdin.readline().rstrip().split()))
    visited = [False] * (N + 1)
    result = 0
    
    for i in range(1, N + 1):
        if (dfs(i) == i):
            result += 1
            
    print(result)