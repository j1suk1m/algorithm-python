from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
scores = sorted(list(float(input()) for _ in range(N)))

for score in scores[:7]:
    print("{:.3f}".format(score))