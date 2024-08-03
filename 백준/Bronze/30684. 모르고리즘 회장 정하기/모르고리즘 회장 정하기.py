from sys import stdin

N = int(stdin.readline().rstrip())
names = sorted(list(stdin.readline().rstrip() for _ in range(N)))

for name in names:
    if len(name) == 3:
        print(name)
        break
