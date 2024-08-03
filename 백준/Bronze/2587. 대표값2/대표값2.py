from sys import stdin

numbers = sorted(list(int(stdin.readline().rstrip()) for _ in range(5)))

print(sum(numbers) // 5)
print(numbers[2])