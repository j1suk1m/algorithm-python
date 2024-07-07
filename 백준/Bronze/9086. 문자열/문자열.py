from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    string = stdin.readline().rstrip()
    print(string[0] + string[-1])