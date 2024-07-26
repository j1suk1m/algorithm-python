from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
stack = deque()

for _ in range(N):
    input = list(map(int, stdin.readline().rstrip().split()))
    operation = input[0]
    
    if operation == 1:
        stack.append(input[1])
    elif operation == 2:
            print(stack.pop()) if len(stack) > 0 else print(-1)
    elif operation == 3:
        print(len(stack))
    elif operation == 4:
        print(1) if len(stack) == 0 else print(0)
    else:
        print(-1) if len(stack) == 0 else print(stack[-1])