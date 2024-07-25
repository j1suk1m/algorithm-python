from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
baskets = [ball for ball in range(0, N + 1)] 

for _ in range(M):
    i, j = map(int, stdin.readline().rstrip().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]
        
print(" ".join(list(map(str, baskets[1:]))))