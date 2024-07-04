from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    R, S = map(str, stdin.readline().rstrip().split())
    
    for letter in S:
        print(letter * int(R), end="")
    
    print()