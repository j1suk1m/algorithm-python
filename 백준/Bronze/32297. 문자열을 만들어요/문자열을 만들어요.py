from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
S = input()

if "gori" in S:
    print("YES")
else:
    print("NO")