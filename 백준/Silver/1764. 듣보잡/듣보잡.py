from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
set1 = set(input() for _ in range(N))
set2 = set(input() for _ in range(M))

answer = sorted(set1.intersection(set2))
print(len(answer))

for name in answer:
    print(name)