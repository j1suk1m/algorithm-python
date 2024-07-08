from sys import stdin

t = int(stdin.readline().rstrip())

for _ in range(t):
    num1, num2 = map(int, stdin.readline().rstrip().split())
    print(num1 + num2)