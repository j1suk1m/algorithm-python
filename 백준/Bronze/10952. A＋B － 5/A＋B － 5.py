from sys import stdin

while True:
    A, B = map(int, stdin.readline().rstrip().split())
    
    if (A == 0 and B == 0):
        break
    else:
        print(A + B)

