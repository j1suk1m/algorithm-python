from sys import stdin

N = int(stdin.readline().rstrip())
numbers = [int(stdin.readline().rstrip()) for _ in range(N)]
numbers.sort()

for number in numbers:
    print(number)