from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

if N == K:
    print(0)
    
else:
    queue = deque([(N - 1, 1), (N + 1, 1), (2 * N, 1)])
    visited = [0] * 100001
    
    ### 너비 우선 탐색 알고리즘
    while queue:
        x, second = queue.popleft()
        
        if x == K:
            print(second)
            break
        
        for dx in [-1, 1, x]:
            nx = x + dx
            
            if nx < 0 or nx > 100000:
                continue
            elif visited[nx] == 0:
                visited[nx] = 1
                queue.append((nx, second + 1))