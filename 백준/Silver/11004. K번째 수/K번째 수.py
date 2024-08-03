from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
A = list(map(int, stdin.readline().rstrip().split()))
A = sorted(A)

print(A[K - 1])