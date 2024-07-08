from sys import stdin

def Rev(X: int):
    X = int("".join(reversed(str(X))))
    return X

X, Y = map(int, stdin.readline().rstrip().split())

print(Rev(Rev(X) + Rev(Y)))