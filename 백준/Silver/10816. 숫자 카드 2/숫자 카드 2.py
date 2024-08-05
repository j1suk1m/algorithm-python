from sys import stdin
from collections import Counter

def binary_search(target, cards):
    start = 0
    end = len(cards) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if cards[mid][0] == target:
            return cards[mid][1]
        elif cards[mid][0] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return 0

N = int(stdin.readline().rstrip())
cards = list(map(int, stdin.readline().rstrip().split()))
cards = sorted(Counter(cards).items())
M = int(stdin.readline().rstrip())
targets = list(map(int, stdin.readline().rstrip().split()))

for target in targets:
    print(binary_search(target, cards), end=" ")