from sys import stdin
from heapq import heappop, heappush

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

def dijkstra(start: int, end: int) -> int:
    queue = []
    weight_list[start] = 0
    heappush(queue, (0, start))
    
    while queue:
        weight, current = heappop(queue)
        
        if weight_list[current] < weight:
            continue
        
        for next in graph[current]:
            next_weight = weight + next[1]
            
            if next_weight < weight_list[next[0]]:
                weight_list[next[0]] = next_weight
                heappush(queue, (next_weight, next[0]))
                
    return weight_list[end]
                
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
weight_list = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

S, T = map(int, input().split())
    
print(dijkstra(S, T))