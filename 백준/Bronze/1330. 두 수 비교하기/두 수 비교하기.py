from sys import stdin

A, B = map(int, stdin.readline().rstrip().split())

if (A > B):
    print(">")
elif (A < B):
    print("<")
else:
    print("==")