from sys import stdin
from collections import Counter

A = int(stdin.readline().rstrip())
B = int(stdin.readline().rstrip())
C = int(stdin.readline().rstrip())

counter = Counter(str(A * B * C))

for i in range(10):
    print(counter[str(i)])