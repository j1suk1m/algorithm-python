from sys import stdin

a = list(map(int, stdin.readline().rstrip().split()))
c = list(map(int, stdin.readline().rstrip().split()))

b = [c[0] - a[2], int(c[1] / a[1]), c[2] - a[0]]
print(" ".join(list(map(str, b))))