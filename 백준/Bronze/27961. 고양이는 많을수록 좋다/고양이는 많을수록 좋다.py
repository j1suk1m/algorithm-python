from sys import stdin

N = int(stdin.readline().rstrip())
result = 0
number = 0

while (number < N):
    if (number * 2 >= number + 1):
        number *= 2
    else:
        number += 1
              
    result += 1
        
print(result)