from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
queue = deque(list(number for number in range(1, N + 1)))
answer = []
count = 1

while queue:
    number = queue.popleft()
    
    if count == K:
        count = 1
        answer.append(number)
    else:
        count += 1
        queue.append(number)
        
print("<" + ", ".join(list(map(str, answer))) + ">")