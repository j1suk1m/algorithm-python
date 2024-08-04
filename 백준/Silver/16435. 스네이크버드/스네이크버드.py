from sys import stdin

N, L = map(int, stdin.readline().rstrip().split())
heights = sorted(list(map(int, stdin.readline().rstrip().split())))

for height in heights:
    if height <= L:
        L += 1
    else:
        break
    
print(L)