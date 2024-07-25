from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
baskets = [ball for ball in range(0, N + 1)] 

for _ in range(M):
    i, j = map(int, stdin.readline().rstrip().split())
    
    for basket in range(i, (i + j) // 2 + 1):
        baskets[basket], baskets[i + j - basket] = baskets[i + j - basket], baskets[basket]
        
print(" ".join(list(map(str, baskets[1:]))))