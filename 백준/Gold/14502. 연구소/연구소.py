from sys import stdin
from copy import deepcopy
from collections import deque

input = lambda: stdin.readline().rstrip()

### 바이러스 전파
def bfs(graph: list) -> int:
    safety_area_count = len(spaces) - 3 ### 안전 영역의 개수
    queue = deque(viruses) ### 바이러스 전체 좌표 삽입
    x, y = viruses[0]
    graph[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if not (0 <= nx < N and 0 <= ny < M):
                continue
            elif graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                safety_area_count -= 1

    return safety_area_count

### 벽 세우기
def back_tracking(count):
    global answer

    if count == 3: ### 벽 3개 세우기 완료
        safety_area_count = bfs(deepcopy(graph)) ### 바이러스 전파
        answer = max(answer, safety_area_count)
        return

    for x, y in spaces:
        if not graph[x][y]:
            graph[x][y] = 1 ### 벽 세우기
            back_tracking(count + 1)
            graph[x][y] = 0 ### 벽 허물기

N, M = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(N))

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
spaces = []
viruses = []
space, virus = 0, 2
answer = 0

### 빈칸 좌표와 바이러스 좌표 각각 저장
for x in range(N):
    for y in range(M):
        if graph[x][y] == space:
            spaces.append((x, y))
        elif graph[x][y] == virus:
            viruses.append((x, y))

back_tracking(0)

print(answer)