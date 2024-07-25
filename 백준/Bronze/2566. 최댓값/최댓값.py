from sys import stdin

numbers = []
maximum = -1

for _ in range(9):
    numbers.append(list(map(int, stdin.readline().rstrip().split())))
    
for row in numbers:
    local_maximum = max(row)
    
    if local_maximum > maximum:
        maximum = local_maximum
        maximum_index = [numbers.index(row) + 1, row.index(local_maximum) + 1]

print(maximum)
print(maximum_index[0], maximum_index[1])