from sys import stdin

N, L, K = map(int, stdin.readline().rstrip().split())
problems = []
score = 0

for _ in range(N):
    sub1, sub2 = map(int, stdin.readline().rstrip().split())
    problems.append((sub1, sub2))
    
problems = sorted(problems, key=lambda sub: (sub[1], sub[0]))

for (sub1, sub2) in problems:
    if K == 0:
        break
    
    if sub2 <= L:
        score += 140
        K -= 1
    elif sub1 <= L < sub2:
        score += 100
        K -= 1
        
print(score)
        