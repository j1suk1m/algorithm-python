from sys import stdin

N = int(stdin.readline().rstrip())
number = 1

while True:
    if ("666" in str(number)):
        N -= 1
    if (N == 0):
        break
    
    number += 1
    
print(number)