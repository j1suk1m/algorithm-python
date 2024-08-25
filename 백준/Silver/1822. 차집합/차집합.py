from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

length = len(A - B)
print(length)

if length:
    print(*sorted(A - B))