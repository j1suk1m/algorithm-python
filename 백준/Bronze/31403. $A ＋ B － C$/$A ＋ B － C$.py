from sys import stdin

A = int(stdin.readline().rstrip())
B = int(stdin.readline().rstrip())
C = int(stdin.readline().rstrip())

print(A + B - C)
print(A * (10 ** len(str(B))) + B - C)