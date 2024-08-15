from sys import stdin
from heapq import heappop, heappush

input = lambda: stdin.readline().rstrip()
INF = int(3e10) + 1

def dijkstra(start: int, end: int) -> int:
    queue = []
    time_list[start] = 0
    heappush(queue, (0, start))
    
    while queue:
        time, current = heappop(queue)
        
        if time_list[current] < time:
            continue
        
        for next in graph[current]:
            next_time = time + next[1]
            
            if next_time < time_list[next[0]]:
                time_list[next[0]] = next_time
                heappush(queue, (next_time, next[0]))
                
    return time_list[end] if time_list[end] < INF else -1
                
N, M = map(int, input().split())
A = list(map(int, input().split()))
graph = [[] for _ in range(N)]
time_list = [INF] * N

for _ in range(M):
    a, b, t = map(int, input().split())
    
    if ((a != N - 1 and A[a] == 1) or
        (b != N - 1 and A[b] == 1)):
        continue
    else:
        graph[a].append((b, t))
        graph[b].append((a, t))
    
print(dijkstra(0, N - 1))