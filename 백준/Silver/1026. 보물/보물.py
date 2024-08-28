from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

answer = sum(map(lambda x: x[0] * x[1], zip(A, B)))
print(answer)