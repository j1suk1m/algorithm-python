from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())

print(N // M)
print(N % M)