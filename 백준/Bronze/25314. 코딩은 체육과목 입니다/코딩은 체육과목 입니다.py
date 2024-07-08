from sys import stdin

N = int(stdin.readline().rstrip())

print("long " * (N // 4) + "int")