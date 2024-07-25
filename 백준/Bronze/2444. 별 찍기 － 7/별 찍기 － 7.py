from sys import stdin

N = int(stdin.readline().rstrip())

for line in range(1, 2 * N):
    if line <= N:
        print(" " * (N - line), end="")
        print("*" * (2 * line - 1))
    else:
        print(" " * (line - N), end="")
        print("*" * (4 * N - 2 * line - 1))