from sys import stdin
from collections import deque

def bfs(number):
    queue = deque([(number, 0)])
    
    while queue:
        number, count = queue.popleft()
        
        number1 = number * 2
        number2 = number * 10 + 1
        
        if number1 == B or number2 == B:
            return count + 2
        if number1 < B:
            queue.append((number1, count + 1))
        if number2 < B:
            queue.append((number2, count + 1))
    
    return -1
        
A, B = map(int, stdin.readline().rstrip().split())

print(bfs(A))