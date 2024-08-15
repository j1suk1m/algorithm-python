from sys import stdin
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    
    if x > 0:
        heappush(heap, x)
    elif x == 0 and len(heap) > 0:
        print(heappop(heap))
    else:
        print(0)