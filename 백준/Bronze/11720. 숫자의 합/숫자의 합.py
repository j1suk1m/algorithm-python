from sys import stdin

N = int(stdin.readline().rstrip())
number_list = list(map(int, list(stdin.readline().rstrip())))

print(sum(number_list))