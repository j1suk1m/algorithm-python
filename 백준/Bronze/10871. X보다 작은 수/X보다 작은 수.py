from sys import stdin

N, X = map(int, stdin.readline().rstrip().split())
number_list = list(map(int, stdin.readline().rstrip().split()))

for number in number_list:
    if (number < X):
        print(number, end=" ")