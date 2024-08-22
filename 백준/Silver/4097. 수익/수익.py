from sys import stdin

input = lambda: stdin.readline().rstrip()

while True:
    N = int(input())
    
    if N == 0:
        break
    elif N == 1:
        print(int(input()))
    else:
        P = list(int(input()) for _ in range(N))
        
        for day in range(1, N):
            P[day] = max(P[day], P[day] + P[day - 1])
            
        print(max(P))