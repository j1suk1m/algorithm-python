from sys import stdin
from heapq import heappop, heappush

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

def dijkstra(start: int):
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
    
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
weight_list = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    
dijkstra(K)

for weight in weight_list[1:]:
    if weight == INF:
        print("INF")
    else:
        print(weight)