from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs() -> int:
    queue = deque([(0, 0)])
    visited[0] = 1
    
    while queue:
        x, count = queue.popleft()
        
        if x == N - 1: ### 가장 오른쪽 칸에 도달한 경우
            return count
        
        for dx in range(1, A[x] + 1):
            nx = x + dx
            
            if nx >= N:
                break
            elif visited[nx]:
                continue
            else:
                visited[nx] = 1
                queue.append((nx, count + 1))
                
    return -1

N = int(input())
A = list(map(int, input().split()))
visited = [0] * N

print(bfs())