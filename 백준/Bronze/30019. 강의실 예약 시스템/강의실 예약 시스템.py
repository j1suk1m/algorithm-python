from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
reservations = dict()

for _ in range(M):
    k, s, e = map(int, stdin.readline().rstrip().split())
    
    if (k in reservations.keys() and reservations[k] > s):
        print("NO")
    else:
        reservations[k] = e
        print("YES")