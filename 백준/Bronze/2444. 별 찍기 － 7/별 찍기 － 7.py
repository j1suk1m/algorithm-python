from sys import stdin

N = int(stdin.readline().rstrip())

for line in range(1, N + 1):
    print(" " * (N - line) + "*" * (2 * line - 1))
for line in range(1, N):
    print(" " * line + "*" * (2 * N - 1 - 2 * line))