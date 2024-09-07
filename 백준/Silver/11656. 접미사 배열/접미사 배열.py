from sys import stdin

input = lambda: stdin.readline().rstrip()

S = input()
suffixes = list(S[index:] for index in range(len(S)))
suffixes.sort()

for suffix in suffixes:
    print(suffix)