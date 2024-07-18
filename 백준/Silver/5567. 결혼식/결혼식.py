from sys import stdin

def bfs(node):
    visited[node] = 1
    friends = set()
    
    for next in graph[node]:
        friends.add(next)
        
        for after_next in graph[next]:
            if not visited[after_next]:
                visited[after_next] = 1
                friends.add(after_next)

    return len(friends)

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, stdin.readline().rstrip().split())
    
    graph[a].append(b)
    graph[b].append(a)
        
print(bfs(1))