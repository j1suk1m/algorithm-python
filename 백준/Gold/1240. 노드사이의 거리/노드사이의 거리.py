from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(start_node: int, end_node: int):
    visited = [0] * (N + 1)
    visited[start_node] = 1 ### 방문 처리
    queue = deque([(start_node, 0)]) ### (노드 번호, 누적 거리)

    while queue:
        current_node, current_dist = queue.popleft()
        
        if current_node == end_node:
            return current_dist
        else:
            for next_node, next_dist in graph[current_node]:
                if not visited[next_node]:
                    visited[next_node] = 1 ### 방문 처리
                    queue.append((next_node, current_dist + next_dist)) ### (노드 번호, 누적 거리)
                    
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

### 연결 관계 저장
for _ in range(N - 1):
    node1, node2, dist = map(int, input().split())
    graph[node1].append((node2, dist))
    graph[node2].append((node1, dist))
    
### 너비 우선 탐색 실행
for _ in range(M):
    node1, node2 = map(int, input().split())
    print(bfs(node1, node2))