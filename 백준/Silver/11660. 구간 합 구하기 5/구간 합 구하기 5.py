from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
table = [[0] * (N + 1)] + list(([0] + list(map(int, input().split()))) for _ in range(N))
prefix_sum = [[0] * (N + 1) for _ in range(N + 1)]

prefix_sum[1][1] = table[1][1]

### 누적 합
for x in range(1, N + 1):
    for y in range(1, N + 1):
        prefix_sum[x][y] = prefix_sum[x - 1][y] + prefix_sum[x][y - 1] - prefix_sum[x - 1][y - 1] + table[x][y]

### 구간 합
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    if x1 == x2 and y1 == y2:
        print(table[x1][y2])
    else:
        print(prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2] - prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1])