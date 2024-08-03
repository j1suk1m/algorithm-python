from sys import stdin
from collections import defaultdict

N = int(stdin.readline().rstrip())
number_dict = defaultdict(int) ### 기본값 0으로 설정

for _ in range(N):
    number = int(stdin.readline().rstrip())
    number_dict[number] += 1
    
number_dict = sorted(number_dict.items())

for key, value in number_dict:
    for _ in range(value):
        print(key)