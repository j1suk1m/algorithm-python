from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
scores = list(tuple(list(map(int, input().split()))) for _ in range(N))
winners = []

for subject in range(4):
    sorted_scores = sorted(scores, key=lambda score: (-score[subject + 1], score[0]))
    
    while sorted_scores[0][0] in winners:
        sorted_scores.pop(0)
        
    winners.append(sorted_scores[0][0])
    
print(*winners)