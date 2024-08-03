from sys import stdin

N, k = map(int, stdin.readline().rstrip().split())
scores = sorted(list(map(int, stdin.readline().rstrip().split())), reverse=True)

print(scores[k - 1])