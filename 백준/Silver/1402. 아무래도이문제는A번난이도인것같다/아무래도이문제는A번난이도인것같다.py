from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    print("yes")