from sys import stdin

N = int(stdin.readline().rstrip())
numbers = list(map(int, stdin.readline().rstrip().split()))

print(*sorted(numbers))