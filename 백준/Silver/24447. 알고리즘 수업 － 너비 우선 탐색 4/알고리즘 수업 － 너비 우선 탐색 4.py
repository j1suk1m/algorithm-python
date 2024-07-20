from sys import stdin
from collections import deque

def bfs(E, R):
    order = 1 ### 전체 방문 순서
    visited = [[0, -1] for _ in range(N + 1)] ### 노드의 방문 순서, 노드의 깊이
    visited[R] = [1, 0] ### 시작 노드의 방문 순서와 깊이
    queue = deque([R])
    
    while queue:
        u = queue.popleft()
        u_depth = visited[u][1] ### 현재 방문한 노드의 깊이
        
        for v in E[u]:
            if not visited[v][0]: ### 방문 순서가 0인 경우, 즉 아직 방문하지 않은 경우
                order += 1
                visited[v] = [order, u_depth + 1]
                queue.append(v)
                
    return visited

N, M, R = map(int, stdin.readline().rstrip().split())
E = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, stdin.readline().rstrip().split())
    
    E[u].append(v)
    E[v].append(u)
    
### 인접 정점을 오름차순으로 방문하기 위한 정렬
for edge in E:
    edge.sort() 
    
visited = bfs(E, R)
print(sum(list(map(lambda node: node[0] * node[1], visited[1:]))))