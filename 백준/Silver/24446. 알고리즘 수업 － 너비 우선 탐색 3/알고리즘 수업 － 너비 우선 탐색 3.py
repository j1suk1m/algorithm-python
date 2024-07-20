### 시작 노드의 깊이가 0이 되어야 하지만, 노드의 방문 처리와 깊이를 visited 리스트에서 동시에 처리하기 위해 시작 노드의 깊이를 1로 설정함
### 따라서 전체 노드의 깊이가 1씩 큰 상태로 visited에 저장되므로, 마지막에 1씩 빼준 뒤 결과를 출력함

from sys import stdin
from collections import deque

def bfs(node):
    visited[node] = 1
    queue = deque([node])
    
    while queue:
        current = queue.popleft()
        
        for next in graph[current]:
            if not visited[next]:
                visited[next] = visited[current] + 1 ### 방문 처리
                queue.append(next)

N, M, R = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    u, v = map(int, stdin.readline().rstrip().split())
    
    graph[u].append(v)
    graph[v].append(u)
    
bfs(R)
print("\n".join(list(map(str, map(lambda depth: depth - 1, visited[1:])))))