from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(start: list, end: list):
    start_z, start_x, start_y = start
    end_z, end_x, end_y = end
    graph[start_z][start_x][start_y] = "#" ### 방문 처리
    queue = deque([(start_z, start_x, start_y, 0)])
    
    while queue:
        z, x, y, time = queue.popleft()
        
        ### 출구 발견
        if z == end_z and x == end_x and y == end_y:
            return "Escaped in {} minute(s).".format(time)
        
        ### 동, 서, 남, 북, 상, 하 이동
        for dz, dx, dy in zip(dzs, dxs, dys):
            nz = z + dz
            nx = x + dx
            ny = y + dy
            
            if not (0 <= nz < L and 0 <= nx < R and 0 <= ny < C):
                continue
            elif graph[nz][nx][ny] != "#":
                graph[nz][nx][ny] = "#"
                queue.append((nz, nx, ny, time + 1))
        
    return "Trapped!"

dzs = [0, 0, 0, 0, -1, 1]
dxs = [0, 0, 1, -1, 0, 0]
dys = [1, -1, 0, 0, 0, 0]
S = [0, 0, 0]
E = [0, 0, 0]

while True:
    L, R, C = map(int, input().split())
    
    ### 종료 조건
    if L == 0 and R == 0 and C == 0:
        break
    else:
        graph = [[[] for x in range(R)] for z in range(L)]

        for z in range(L):
            for x in range(R):
                row = list(input())
                
                ### 시작 지점 및 출구의 인덱스 저장
                for y in range(C):
                    if row[y] == "S":
                        S = [z, x, y]
                    elif row[y] == "E":
                        E = [z, x, y]
                        
                graph[z][x] = row

            input()
            
        ### 너비 탐색 알고리즘 실행
        print(bfs(S, E))