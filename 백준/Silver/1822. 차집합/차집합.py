from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
difference_set = A - B

print(len(difference_set))

if len(difference_set):
    print(*sorted(difference_set))