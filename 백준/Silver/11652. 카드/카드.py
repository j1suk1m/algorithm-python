from sys import stdin
from collections import Counter

input = lambda: stdin.readline().rstrip()

N = int(input())
cards = list(int(input()) for _ in range(N))
counter = sorted(Counter(cards).most_common(), key=lambda x: (-x[1], x[0]))

print(counter[0][0])