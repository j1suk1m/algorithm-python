from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    before_cards = list(map(str, input().split()))
    after_cards = list(map(str, input().split()))
    
    if sorted(before_cards) == sorted(after_cards):
        print("NOT CHEATER")
    else:
        print("CHEATER")