from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]
answer = []

### 연결 관계 저장
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1
    
### 플로이드 워셜 알고리즘
for k in range(1, N + 1):
    graph[k][k] = 0
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
### (건물 번호1, 건물 번호2, 접근성의 합) 튜플 저장
for col_1 in range(1, N):
    for col_2 in range(col_1 + 1, N + 1):
        total_cost = 0 ### 접근성의 합
        
        for row in range(1, N + 1):
            if row == col_1 or row == col_2:
                continue
            else: ### 가장 가까운 건물까지 왕복하는 최단 시간의 총합
                total_cost += 2 * min(graph[row][col_1], graph[row][col_2])
        
        answer.append((col_1, col_2, total_cost))
        
answer = sorted(answer, key=lambda x: (x[2], x[0], x[1]))
print(*answer[0])