from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

def bfs():
    queue = deque(viruses)

    while queue:
        x, y, virus, second = queue.popleft()

        if second >= S:
            break

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                queue.append((nx, ny, virus, second + 1))

    return graph[X - 1][Y - 1]

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
viruses = []

for x in range(N):
    for y in range(N):
        if graph[x][y] > 0:
            viruses.append((x, y, graph[x][y], 0))

viruses = sorted(viruses, key=lambda x: x[2])

print(bfs())