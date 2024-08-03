from sys import stdin

N = int(stdin.readline().rstrip())
scores = []

for _ in range(N):
    input = list(map(int, stdin.readline().rstrip().split()))
    scores.append(max(input[:2]) + sum(sorted(input[2:], reverse=True)[:2]))
    
scores.sort(reverse=True)
print(scores[0])