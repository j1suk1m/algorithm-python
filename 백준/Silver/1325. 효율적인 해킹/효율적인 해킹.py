from sys import stdin
from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = 1
    count = 1
    
    while queue:
        node = queue.popleft()
        count += 1
        
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1
            
    return count
    
N, M = map(int, stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
answers = []
count = -1

for _ in range(M):
    A, B = map(int, stdin.readline().rstrip().split()) ### A가 B를 신뢰
    graph[B].append(A) ### B를 해킹하면 A도 해킹 가능

for node in range(1, N + 1):
    visited = [0] * (N + 1)
    search_result = bfs(node)
    
    if search_result > count:
        answers = [node]
        count = search_result
    elif search_result == count:
        answers.append(node)

answers.sort()
            
print(" ".join(list(map(str, answers))))