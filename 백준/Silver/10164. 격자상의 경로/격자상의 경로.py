from sys import stdin

### 다이나믹 프로그래밍
def get_path_count(end_x: int, end_y: int) -> int:
    start_x, start_y = 1, 1
    
    for x in range(start_x, end_x + 1):
        for y in range(start_y, end_y + 1):
            if x == 1 and y == 1 :
                continue
            
            graph[x][y] = graph[x][y - 1] + graph[x - 1][y]
            
    return graph[end_x][end_y]

input = lambda: stdin.readline().rstrip()

N, M, K = map(int, input().split())
mandatory_point = (K // M + 1, K - (K // M) * M) ### 동그라미로 표시된 칸의 좌표
answer = 1

if K == 0:
    end_points = [(N, M)]
else:
    end_points = [mandatory_point, (N - mandatory_point[0] + 1, M - mandatory_point[1] + 1)]

for end_x, end_y in end_points:
    graph = [[0] * (end_y + 1) for _ in range(end_x + 1)]
    graph[1][1] = 1
    answer *= get_path_count(end_x, end_y)

print(answer)