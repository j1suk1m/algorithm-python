from sys import stdin

N = int(stdin.readline().rstrip())
numbers = [int(stdin.readline().rstrip()) for _ in range(N)]
numbers.sort(reverse=True)

for number in numbers:
    print(number)