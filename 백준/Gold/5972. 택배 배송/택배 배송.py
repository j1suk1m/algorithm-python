from sys import stdin
from heapq import heappop, heappush

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

def dijkstra(start: int, end: int) -> int:
    queue = []
    cost_list[start] = 0
    heappush(queue, (0, start))
    
    while queue:
        cost, current = heappop(queue)
        
        if cost_list[current] < cost:
            continue
        
        for next in graph[current]:
            next_cost = cost + next[1]
            
            if next_cost < cost_list[next[0]]:
                cost_list[next[0]] = next_cost
                heappush(queue, (next_cost, next[0]))
                
    return cost_list[end]
                
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
cost_list = [INF] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
    
print(dijkstra(1, N))