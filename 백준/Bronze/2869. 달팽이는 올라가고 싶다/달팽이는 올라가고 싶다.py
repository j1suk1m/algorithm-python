from sys import stdin
from math import ceil

A, B, V = map(int, stdin.readline().rstrip().split())

print(ceil((V - A) / (A - B)) + 1)