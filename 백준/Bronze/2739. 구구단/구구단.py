from sys import stdin

N = int(stdin.readline().rstrip())

for i in range(1, 10):
    print("{} * {} = {}".format(N, i, N * i))