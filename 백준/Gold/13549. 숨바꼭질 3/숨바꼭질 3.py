from sys import stdin
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

def dijkstra(start: int, end: int):
    times[start] = 0
    heap = []
    heappush(heap, (0, start))
    
    while heap:
        current_time, current_pos = heappop(heap)
        
        if current_pos == end:
            return current_time
        elif times[current_pos] < current_time:
            continue
        else:
            for move, cost in [(-1, 1), (1, 1), (current_pos, 0)]:
                next_pos = current_pos + move
                next_time = current_time + cost

                if 0 <= next_pos <= 100000 and next_time < times[next_pos]:
                    times[next_pos] = next_time
                    heappush(heap, (next_time, next_pos))
                
N, K = map(int, input().split())
times = [INF] * (100001)

print(dijkstra(N, K))