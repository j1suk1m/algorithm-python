from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())
sum = sum((a, b, c))
max = max((a, b, c))

if max >= sum - max: 
    print(2 * (sum - max) - 1)
else:
    print(sum)