from sys import stdin
from itertools import combinations

N, K = map(int, stdin.readline().rstrip().split())
answers = list(combinations(range(N), K))

print(len(answers))