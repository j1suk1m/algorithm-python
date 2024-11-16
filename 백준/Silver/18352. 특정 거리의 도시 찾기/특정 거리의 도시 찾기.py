from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

def bfs(node: int) -> list:
    answer = []
    queue = deque([(node, 0)])
    visited[node] = 1

    while queue:
        node, distance = queue.popleft()

        if distance == K:
            answer.append(node)
        elif distance > K:
            break

        for next in graph[node]:
            if not visited[next]:
                queue.append((next, distance + 1))
                visited[next] = 1

    return sorted(answer)

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

answer = bfs(X)

if not answer:
    print(-1)
else:
    for node in answer:
        print(node)