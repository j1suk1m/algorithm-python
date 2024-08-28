from sys import stdin
from math import sqrt

input = lambda: stdin.readline().rstrip()

N = int(input())
square_root = sqrt(N)
number = 1

### 약수의 개수가 홀수인 수, 즉 제곱수의 개수 찾기
while number <= square_root:
    number += 1
    
print(number - 1)