from sys import stdin
from bisect import bisect_left, bisect_right

n, m = map(int, stdin.readline().rstrip().split())
A = sorted(list(map(int, stdin.readline().rstrip().split())))

for _ in range(m):
    B = list(map(int, stdin.readline().rstrip().split()))
    operation = B[0]
    
    if operation == 1:
        print(n - bisect_left(A, B[1]))
    elif operation == 2:
        print(n - bisect_right(A, B[1]))
    else:
        print(bisect_right(A, B[2]) - bisect_left(A, B[1]))