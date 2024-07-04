from sys import stdin

num_list = []

for _ in range(10):
    num_list.append(int(stdin.readline().rstrip()) % 42)
            
print(len(set(num_list)))