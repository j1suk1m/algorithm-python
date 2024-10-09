from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(start: int, end: int) -> int:
    queue = deque([(start, 0)])
    visited[start] = 1
    
    while queue:
        char, count = queue.popleft()
        
        if char == end:
            return count
        
        for next in graph[char]:
            if not visited[next]:
                queue.append((next, count + 1))
                visited[next] = 1
                
    return -1

A, B = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

### 연결 관계 저장
for _ in range(M):
    char1, char2 = map(int, input().split())
    graph[char1].append(char2)
    graph[char2].append(char1)

### 너비 우선 탐색 실행
print(bfs(A, B))