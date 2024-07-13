from sys import stdin

S = int(stdin.readline().rstrip())
num = 1
sum = 0

while sum < S:
    sum += num
    num += 1

print(num - 2) if sum > S else print(num - 1)