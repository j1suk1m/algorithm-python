from sys import stdin

N = int(stdin.readline().rstrip())
sizes = list(map(int, stdin.readline().rstrip().split()))
T, P = map(int, stdin.readline().rstrip().split())
answer = 0

for size in sizes:
    answer += (size - 1) // T + 1
    
print(answer)
print(N // P, N % P)