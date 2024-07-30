from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
queue = deque()

for _ in range(N):
    try:
        operations = stdin.readline().rstrip().split()
        operation = operations[0]
    
        if operation == "push":
            queue.append(operations[1])
        elif operation == "pop":
            print(queue.popleft()) 
        elif operation == "size":
            print(len(queue))
        elif operation == "empty":
            print(1) if len(queue) == 0 else print(0)
        elif operation == "front":
            print(queue[0]) 
        else:
            print(queue[-1]) 
    except:
        print(-1)