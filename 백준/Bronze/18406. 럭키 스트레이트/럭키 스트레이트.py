from sys import stdin

N = list(map(int, list(stdin.readline().rstrip())))
mid = len(N) // 2

if sum(N[0:mid]) == sum(N[mid:]):
    print("LUCKY")
else:
    print("READY")