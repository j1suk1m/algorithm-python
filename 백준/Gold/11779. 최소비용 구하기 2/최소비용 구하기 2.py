from sys import stdin
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

### 다익스트라 알고리즘
def dijkstra(start: int, end: int):
    queue = []
    cost_list[start] = 0
    heappush(queue, (0, start, [start]))
    
    while queue:
        cost, current, path_list = heappop(queue)
        
        ### 목표 지점에 도달
        if current == end:
            return path_list
        
        if cost_list[current] < cost:
            continue
        
        ### 최소 비용 갱신
        for next in graph[current]:
            next_cost = cost + next[1]
            
            if next_cost < cost_list[next[0]]:
                cost_list[next[0]] = next_cost
                next_path_list = path_list + [next[0]]
                heappush(queue, (next_cost, next[0], next_path_list))

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
cost_list = [INF] * (N + 1)

### 연결 관계 저장
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    
target_start, target_end = map(int, input().split())
path_list = dijkstra(target_start, target_end)

print(cost_list[target_end])
print(len(path_list))
print(*path_list)