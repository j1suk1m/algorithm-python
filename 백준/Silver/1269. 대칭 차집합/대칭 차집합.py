from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

print(N + M - 2 * len(A & B))