from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

N = int(input())
queue = deque()

for _ in range(N):
    operations = input().split()
    operation = operations[0]
    
    if operation == "push":
        queue.append(operations[1])
    elif operation == "pop":
        print(queue.popleft()) if len(queue) > 0 else print(-1)
    elif operation == "size":
        print(len(queue))
    elif operation == "empty":
        print(1) if len(queue) == 0 else print(0)
    elif operation == "front":
        print(queue[0]) if len(queue) > 0 else print(-1)
    else:
        print(queue[-1]) if len(queue) > 0 else print(-1)