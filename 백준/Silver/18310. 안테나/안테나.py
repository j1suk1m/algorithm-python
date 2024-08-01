from sys import stdin

N = int(stdin.readline().rstrip())
positions = sorted(list(map(int, stdin.readline().rstrip().split())))
print(positions[(len(positions) - 1) // 2])