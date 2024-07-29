from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 5 * 2)

def dfs(node):
    global order
    order += 1
    visited[node] = order
    
    for next in graph[node]:
        if not visited[next]:
            dfs(next)
    
N, M, R = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
order = 0

for _ in range(M):
    u, v = map(int, stdin.readline().rstrip().split())
    
    graph[u].append(v)
    graph[v].append(u)
    
for edge in graph:
    edge.sort(reverse=True)
    
dfs(R)
print("\n".join(list(map(str, visited[1:]))))