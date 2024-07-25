from sys import stdin

X = int(stdin.readline().rstrip())
N = int(stdin.readline().rstrip())

for _ in range(N):
    a, b = map(int, stdin.readline().rstrip().split())
    X -= (a * b)
    
if (X):
    print("No")
else:
    print("Yes")