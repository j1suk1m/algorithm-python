from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

N = int(input())
deq = deque()

for _ in range(N):
    operations = input().split()
    operation = operations[0]
    
    if operation == "push_front":
        deq.appendleft(operations[1])
    elif operation == "push_back":
        deq.append(operations[1])
    elif operation == "pop_front":
        print(deq.popleft()) if len(deq) > 0 else print(-1)
    elif operation == "pop_back":
        print(deq.pop()) if len(deq) > 0 else print(-1)
    elif operation == "size":
        print(len(deq))
    elif operation == "empty":
        print(1) if len(deq) == 0 else print(0)
    elif operation == "front":
        print(deq[0]) if len(deq) > 0 else print(-1)
    else:
        print(deq[-1]) if len(deq) > 0 else print(-1)