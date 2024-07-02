from sys import stdin

N = int(stdin.readline().rstrip())
cards = list(map(int, stdin.readline().rstrip().split()))
target = 1
result = 0

for card in cards:
    if (card == target):
        result += 1
        target += 1

print(len(cards) - result)