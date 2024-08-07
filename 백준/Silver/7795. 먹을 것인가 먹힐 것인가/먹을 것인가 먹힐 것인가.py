from sys import stdin
from bisect import bisect_left

T = int(stdin.readline().rstrip())

for _ in range(T):
    N, M = map(int, stdin.readline().rstrip().split())
    A = list(map(int, stdin.readline().rstrip().split()))
    B = sorted(list(map(int, stdin.readline().rstrip().split())))
    answer = 0
    
    for a in A:
        answer += bisect_left(B, a)
        
    print(answer)