from sys import stdin

n = int(stdin.readline().rstrip())
length_list = sorted(list(map(int, stdin.readline().rstrip().split())))
left_length = sum(length_list) 
cost = 0

for i in range(n - 1):
    current_length = length_list[i]
    left_length -= current_length
    cost += (current_length * left_length)
    
print(cost)