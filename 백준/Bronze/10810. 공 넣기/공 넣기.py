from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
baskets = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, stdin.readline().rstrip().split())
    
    for basket in range(i, j + 1):
        baskets[basket] = k
        
print(" ".join(list(map(str, baskets[1:]))))