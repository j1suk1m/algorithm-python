from sys import stdin
from math import sqrt

input = lambda: stdin.readline().rstrip()

M, N = map(int, input().split())
numbers = ([0] * 2) + ([1] * (N - 1))

for number in range(2, int(sqrt(N)) + 1):
    if numbers[number] == 1:
        for multiple in range(number * 2, N + 1, number):
            numbers[multiple] = 0
                
for number in range(M, N + 1):
    if numbers[number] == 1:
        print(number)