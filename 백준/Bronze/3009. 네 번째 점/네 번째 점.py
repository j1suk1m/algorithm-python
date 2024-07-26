from sys import stdin
from collections import Counter

x_list = []
y_list = []

for _ in range(3):
    x, y = map(int, stdin.readline().rstrip().split())
    
    x_list.append(x)
    y_list.append(y)
    
x_counter = Counter(x_list)
y_counter = Counter(y_list)

print(x_counter.most_common(2)[1][0], y_counter.most_common(2)[1][0])