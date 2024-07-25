from sys import stdin

number_1, number_2, number_3 = map(int, stdin.readline().rstrip().split())
numbers = [0] * 7

for number in [number_1, number_2, number_3]:
    numbers[number] += 1
    
if 3 in numbers:
    print(10000 + numbers.index(3) * 1000)
elif 2 in numbers:
    print(1000 + numbers.index(2) * 100)
else:
    print(max(number_1, number_2, number_3) * 100)