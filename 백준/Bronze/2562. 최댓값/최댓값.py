from sys import stdin

line_num = 9
maximum = 0

for i in range(1, line_num + 1):
    number = int(stdin.readline().rstrip())
    
    if (number > maximum):
        maximum = number
        order = i

print(maximum)
print(order)