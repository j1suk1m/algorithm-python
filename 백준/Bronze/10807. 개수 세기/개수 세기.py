from sys import stdin
from collections import Counter

N = int(stdin.readline().rstrip())
number_list = list(map(int, stdin.readline().rstrip().split()))
v = int(stdin.readline().rstrip())

counter = Counter(number_list)

if (v in counter.keys()):
    print(counter[v])
else:
    print("0")