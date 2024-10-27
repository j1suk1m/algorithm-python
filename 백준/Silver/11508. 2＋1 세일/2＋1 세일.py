from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
prices = list(int(input()) for _ in range(N))
sorted_prices = sorted(prices, reverse=True)
answer = 0
index = 0

while index < N - 2:
    answer += (sorted_prices[index] + sorted_prices[index + 1])
    index += 3

answer += sum(sorted_prices[index:])

print(answer)