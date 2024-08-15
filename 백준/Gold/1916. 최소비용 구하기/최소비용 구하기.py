from sys import stdin
from heapq import heappop, heappush

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

def dijkstra(start: int, end: int) -> int:
    queue = []
    cost_list[start] = 0 ### 시작 노드의 비용을 0으로 설정
    heappush(queue, (0, start)) 
    
    while queue:
        cost, current = heappop(queue)
        
        ### 이미 최적의 비용으로 결정된 경우
        if cost_list[current] < cost:
            continue
        
        for next in graph[current]:
            next_cost = cost + next[1]
            
            ### 최적의 비용 갱신
            if next_cost < cost_list[next[0]]:
                cost_list[next[0]] = next_cost
                heappush(queue, (next_cost, next[0]))
                
    return cost_list[end]

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
cost_list = [INF] * (N + 1)

for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    
target_start, target_end = map(int, input().split())

print(dijkstra(target_start, target_end))