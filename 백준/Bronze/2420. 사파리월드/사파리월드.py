from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

print(max(N - M, M - N))