from sys import stdin
from math import sqrt

input = lambda: stdin.readline().rstrip()

K = int(input())
A, B, C, D = map(int, input().split())

result1 = A * K + B
result2 = C * K + D

if result1 == result2:
    print("Yes", result1)
else:
    print("No")