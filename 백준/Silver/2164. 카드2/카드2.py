from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

N = int(input())
queue = deque(list(card for card in range(1, N + 1)))

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())
    
print(queue[0])