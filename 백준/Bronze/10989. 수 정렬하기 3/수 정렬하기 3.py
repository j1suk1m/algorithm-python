from sys import stdin
from collections import defaultdict

N = int(stdin.readline().rstrip())
number_dict = defaultdict(int) ### 기본값 0으로 설정

for _ in range(N):
    number = int(stdin.readline().rstrip())
    number_dict[number] += 1
    
for number in range(1, 10001):
    if N <= 0:
        break
    
    if number_dict[number] > 0:
        for _ in range(number_dict[number]):
            print(number)
    
        N -= 1