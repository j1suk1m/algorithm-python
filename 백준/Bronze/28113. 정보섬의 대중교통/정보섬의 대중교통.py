from sys import stdin

N, A, B = map(int, stdin.readline().rstrip().split())

if (A < B):
    print("Bus")
elif (A == B):
    print("Anything")
else:
    print("Subway")