from sys import stdin

A, B = map(int, stdin.readline().rstrip().split())
C = int(stdin.readline().rstrip())

A += (C // 60)
B += (C % 60)

if B >= 60:
    B -= 60
    A += 1

if A >= 24:
    A -= 24
    
print(A, B)