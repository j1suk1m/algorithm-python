from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
candy = [[0 for _ in range(M + 1)]] + list(([0] + list(map(int, stdin.readline().rstrip().split()))) for _ in range(N))

for x in range(1, N + 1):
    for y in range(1, M + 1):
        candy[x][y] += max(candy[x - 1][y], candy[x][y - 1], candy[x - 1][y - 1])

print(candy[N][M])