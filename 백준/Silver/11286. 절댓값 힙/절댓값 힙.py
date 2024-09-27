from sys import stdin
from heapq import heappush, heappop

input = lambda: stdin.readline().rstrip()

N = int(input())
array = list()

for _ in range(N):
    x = int(input())
    
    if x != 0:
        heappush(array, (abs(x), x))
    elif len(array) > 0:
        print(heappop(array)[1])
    else:
        print(0)