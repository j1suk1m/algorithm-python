from sys import stdin
from math import factorial

N = int(stdin.readline().rstrip())
N_factorial = str(factorial(N))
result = 0

for i in range(len(N_factorial) - 1, 0, -1):
    if (N_factorial[i] == '0'):
        result += 1
    else:
        break
    
print(result)