from sys import stdin

n = int(stdin.readline().rstrip())
sum = 0

while (n > 0):
    sum += n
    n -= 1
    
print(sum)