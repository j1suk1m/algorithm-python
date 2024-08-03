from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    array = sorted(list(map(int, stdin.readline().rstrip().split())), reverse=True)
    print(array[2])