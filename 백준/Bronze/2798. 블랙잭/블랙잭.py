from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
cards = list(map(int, stdin.readline().rstrip().split()))
max = 0

for card_1 in range(N - 2):
    for card_2 in range(card_1 + 1, N - 1):
        for card_3 in range(card_2 + 1, N):
            sum = cards[card_1] + cards[card_2] + cards[card_3]
            
            if max < sum <= M:
                max = sum
                
print(max)