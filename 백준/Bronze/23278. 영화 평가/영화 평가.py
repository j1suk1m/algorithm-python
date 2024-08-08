from sys import stdin

N, L, H = map(int, stdin.readline().rstrip().split())
scores = sorted(list(map(int, stdin.readline().rstrip().split())))

print(sum(scores[L : N - H]) / (N - (L + H)))