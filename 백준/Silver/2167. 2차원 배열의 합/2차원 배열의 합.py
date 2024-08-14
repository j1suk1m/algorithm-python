from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
array = [[0] * (M + 1)] + list(([0] + list(map(int, stdin.readline().rstrip().split()))) for _ in range(N))
K = int(stdin.readline().rstrip())
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

for row in range(1, N + 1):
    for col in range(1, M + 1):
        prefix_sum[row][col] = prefix_sum[row - 1][col] + prefix_sum[row][col - 1] - prefix_sum[row - 1][col - 1] + array[row][col]

for _ in range(K):
    i, j, x, y = map(int, stdin.readline().rstrip().split())
    answer = prefix_sum[x][y] - prefix_sum[i - 1][y] - prefix_sum[x][j - 1] + prefix_sum[i - 1][j - 1]
    print(answer)