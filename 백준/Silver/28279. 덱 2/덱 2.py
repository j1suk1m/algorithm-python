from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
deq = deque()

for _ in range(N):
    operations = list(map(int, stdin.readline().rstrip().split()))
    operation_type = operations[0]
    
    try:
        if operation_type == 1:
            deq.appendleft(operations[1])
        elif operation_type == 2:
            deq.append(operations[1])
        elif operation_type == 3:
            print(deq.popleft())
        elif operation_type == 4:
            print(deq.pop())
        elif operation_type == 5:
            print(len(deq))
        elif operation_type == 6:
            print(1) if len(deq) == 0 else print(0)
        elif operation_type == 7:
            print(deq[0])
        else:
            print(deq[-1])
    except IndexError:
        print(-1)