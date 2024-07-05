from sys import stdin

N = int(stdin.readline().rstrip())
number_list = list(map(int, stdin.readline().rstrip().split()))

print(min(number_list), max(number_list))