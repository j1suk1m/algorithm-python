from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    input()
    string = sorted(list(map(int, input())), reverse=True)
    
    print(int("".join(list(map(str, string[:-1])))) + int(string[-1]))