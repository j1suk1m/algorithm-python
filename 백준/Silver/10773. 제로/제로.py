from sys import stdin
from collections import deque

K = int(stdin.readline().rstrip())
stack = deque()

for _ in range(K):
    number = int(stdin.readline().rstrip())
    
    if number:
        stack.append(number)
    else:
        stack.pop()
        
print(sum(stack))