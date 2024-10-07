from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

### 너비 우선 탐색 알고리즘
def bfs(space_number: int) -> int:
    visited[space_number] = 1
    queue.append((space_number, 0))
    
    while queue:
        space_number, count = queue.popleft()
        
        if space_number == 100:
            return count
        
        for dice in range(1, 7): ### 주사위 굴리기
            next_space_number = space_number + dice
            
            if next_space_number > 100:
                break
            elif visited[next_space_number]:
                continue
            elif next_space_number in move.keys(): ### 이동한 칸에 사다리 또는 뱀이 있는 경우
                visited[next_space_number] = 1
                visited[move[next_space_number]] = 1
                queue.append((move[next_space_number], count + 1))
            else: ### 이동한 칸에 숫자만 있는 경우
                visited[next_space_number] = 1
                queue.append((next_space_number, count + 1))
                
N, M = map(int, input().split())
queue = deque()
move = dict()
visited = [0] * 101

### 사다리 정보 저장
for _ in range(N):
    x, y = map(int, input().split())
    move[x] = y
    
### 뱀 정보 저장
for _ in range(M):
    u, v = map(int, input().split())
    move[u] = v

### 너비 우선 탐색 실행   
print(bfs(1))