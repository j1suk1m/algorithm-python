from sys import stdin

input = lambda: stdin.readline().rstrip()

N = list(map(int, list(input())))
numbers = [0] * 10

for number in N:
    numbers[number] += 1
    
answer = (numbers[6] + numbers[9]) // 2 + (numbers[6] + numbers[9]) % 2
numbers[6] = 0
numbers[9] = 0

answer = max(answer, max(numbers))

print(answer)