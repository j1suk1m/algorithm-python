from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M, K = map(int, input().split())
scores = dict()
answer = 0

for _ in range(N):
    subject, score = map(str, input().split())
    scores[subject] = int(score)
    
for _ in range(K):
    subject = input()
    answer += scores[subject]
    del scores[subject]
    
sorted_scores = sorted(scores.values())

print(answer + sum(sorted_scores[:M - K]), answer + sum(sorted_scores[N - M:]))