from sys import stdin

numbers = sorted(list(map(int, stdin.readline().rstrip().split())))
print(numbers[0], numbers[1], numbers[2])