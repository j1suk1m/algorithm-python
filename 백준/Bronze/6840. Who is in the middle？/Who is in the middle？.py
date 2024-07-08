from sys import stdin

bowl_list = []

for _ in range(3):
    bowl_list.append(int(stdin.readline().rstrip()))
    
bowl_list.sort()
print(bowl_list[1])