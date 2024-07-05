from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    print(sum(list(map(int, stdin.readline().rstrip().split()))))