from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(start: int, end: int):
    queue = deque([(start, 0)])
    visited[start] = 1
    
    while queue:
        current, count = queue.popleft()
        current_stone_number = stepping_stones[current]
        
        if current == end:
            return count
        
        for move in range(current_stone_number, N + 1, current_stone_number):
            for next in (current + move, current - move):
                if not (0 < next <= N):
                    continue
                elif not visited[next]:
                    visited[next] = 1
                    queue.append((next, count + 1))
                
    return -1

N = int(input())
stepping_stones = [0] + list(map(int, input().split()))
A, B = map(int, input().split())
visited = [0] * (N + 1)

### 너비 우선 탐색 알고리즘 실행
print(bfs(A, B))