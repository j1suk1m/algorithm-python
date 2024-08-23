from sys import stdin
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()

N = int(input())
heap = []

for _ in range(N):
    X = int(input())
    
    if X:
        heappush(heap, -X)
    elif len(heap) > 0:
        print(-heappop(heap))
    else:
        print(0)