from sys import stdin
from collections import deque

def bfs(x, y, isColorBlind: bool):
    queue = deque([(x, y)])
    color = graph[x][y]
    graph[x][y] = color.swapcase() ### 대소문자 변환을 이용한 방문 처리
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            
            if (0 <= nx < N and 0 <= ny < N):
                next_color = graph[nx][ny]
                
                if ((next_color == color) or ### 적록색약 여부와 관계 없이 색깔이 동일한 경우
                    (isColorBlind and abs(ord(next_color) - ord(color)) == 11)): ### 적록색약이고 아스키코드의 차가 11인 경우(r과 g)
                        queue.append((nx, ny))
                        graph[nx][ny] = color.swapcase() ### 대소문자 변환을 이용한 방문 처리

    return 1    
    
N = int(stdin.readline().rstrip())
graph = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

for _ in range(N):
    graph.append(list(stdin.readline().rstrip()))
    
for case in range(1, 3):
    result = 0
    
    for x in range(N):
        for y in range(N):
            if (case == 1 and graph[x][y].isupper()): ### 적록색약이 아닌 경우의 탐색
                result += bfs(x, y, False)
            elif (case == 2 and graph[x][y].islower()): ### 적록색약인 경우의 탐색
                result += bfs(x, y, True)
                
    print(result, end=" ")