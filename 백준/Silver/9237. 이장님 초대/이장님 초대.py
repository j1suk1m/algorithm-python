from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
T = list(map(int, input().split()))

T.sort(reverse=True)

for tree in range(N):
    T[tree] += (tree + 1)
    
print(max(T) + 1)