from sys import stdin

number = list(map(int, list(stdin.readline().rstrip())))
number = sorted(number, reverse=True)

print("".join(list(map(str, number))))