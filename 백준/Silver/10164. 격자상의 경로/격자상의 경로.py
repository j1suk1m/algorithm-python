from sys import stdin

input = lambda: stdin.readline().rstrip()

### 다이나믹 프로그래밍
def get_path_count(end_x: int, end_y: int) -> int:
    start_x, start_y = 1, 1
    
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if x == 1 and y == 1 :
                continue
            
            graph[x][y] = graph[x][y - 1] + graph[x - 1][y]
            
    return graph[end_x][end_y]

N, M, K = map(int, input().split())
answer = 1

if K == 0:
    end_points = [(N, M)]
else:
    mandatory_point = ((K - 1) // M + 1, K - ((K - 1) // M * M)) ### 동그라미로 표시된 칸의 좌표
    mandatory_x, mandatory_y = mandatory_point

    if mandatory_x == 1 or mandatory_y == 1:
        end_points = [(N - mandatory_x + 1, M - mandatory_y + 1)]
    elif mandatory_x == N or mandatory_y == M:
        end_points = [mandatory_point]
    else:
        end_points = [mandatory_point, (N - mandatory_x + 1, M - mandatory_y + 1)]

for end_x, end_y in end_points:
    graph = [[0] * (end_y + 1) for _ in range(end_x + 1)]
    graph[1][1] = 1
    answer *= get_path_count(end_x, end_y)

print(answer)