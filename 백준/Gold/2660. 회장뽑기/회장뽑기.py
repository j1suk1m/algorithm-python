from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
answer = []

### 연결 관계 저장
while True:
    member1, member2 = map(int, input().split())
    
    if member1 == -1 and member2 == -1:
        break
    else:
        graph[member1][member2] = 1
        graph[member2][member1] = 1
        
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    graph[k][k] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
### (최종 점수, 회원 번호) 튜플 저장
for idx, scores in enumerate(graph[1:]):
    answer.append((max(scores[1:]), idx + 1))
        
### 회장 후보 선출
answer = sorted(answer, key=lambda x: (x[0], x[1]))
minimum_score = answer[0][0]
candidates = [number for score, number in answer if score == minimum_score]

print(minimum_score, len(candidates))
print(*candidates)