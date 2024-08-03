from sys import stdin

N = int(stdin.readline().rstrip())
numbers = [0] * 10001

for _ in range(N):
    number = int(stdin.readline().rstrip())
    numbers[number] += 1
    
for number in range(1, 10001):
    if numbers[number] > 0:
        for _ in range(numbers[number]):
            print(number)