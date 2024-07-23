from sys import stdin
from collections import deque

def bfs(S, T):
    queue = deque([(S, T, 0)])
    
    while queue:
        S, T, count = queue.popleft()
        
        if (S + S == T + 3 or S + 1 == T):
            return count + 1
        if (S + S < T + 3):
            queue.append((S + S, T + 3, count + 1))
        if (S + 1 < T):
            queue.append((S + 1, T, count + 1))
        
C = int(stdin.readline().rstrip())

for _ in range(C):
    S, T = map(int, stdin.readline().rstrip().split())
    print(bfs(S, T))