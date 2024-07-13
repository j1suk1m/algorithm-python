from sys import stdin
from math import ceil

N = int(stdin.readline().rstrip())
pizza_list = [0] * 3 ### 3/4, 1/2, 1/4의 개수

for _ in range(N):
    pizza = stdin.readline().rstrip()
    
    if pizza == "3/4":
        pizza_list[0] += 1
    elif pizza == "1/2":
        pizza_list[1] += 1
    else:
        pizza_list[2] += 1
        
result = pizza_list[0] + (pizza_list[1] + 1) // 2
pizza_list[2] -= min(pizza_list[0], pizza_list[2])
pizza_list[2] -= 2 if pizza_list[1] % 2 else 0
result += (pizza_list[2] + 3) // 4

print(result)