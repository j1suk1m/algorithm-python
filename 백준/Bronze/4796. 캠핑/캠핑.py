from sys import stdin

idx = 0

while True:
    L, P, V = map(int, stdin.readline().rstrip().split())
    
    if (L == 0):
        break
    else:
        result = min((V % P), L) + (V // P) * L
        idx += 1
        print("Case {}: {}".format(idx, result))