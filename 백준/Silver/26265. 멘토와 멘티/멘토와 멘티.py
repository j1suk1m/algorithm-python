from sys import stdin

N = int(stdin.readline().rstrip())
pairs = list(tuple(stdin.readline().rstrip().split()) for _ in range(N))
pairs = sorted(sorted(pairs, key=lambda pair: pair[1], reverse=True), key=lambda pair: pair[0])

for pair in pairs:
    print(*pair)