from sys import stdin
from math import sqrt

input = lambda: stdin.readline().rstrip()

N = int(input())
numbers = list(map(int, input().split()))
answer = N

for number in numbers:
    if number <= 2:
        if number == 1:
            answer -= 1
        continue

    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            answer -= 1
            break
        
print(answer)