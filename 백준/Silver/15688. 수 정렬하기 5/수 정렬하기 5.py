from sys import stdin

N = int(stdin.readline().rstrip())
numbers = sorted([int(stdin.readline().rstrip()) for _ in range(N)])

for number in numbers:
    print(number)