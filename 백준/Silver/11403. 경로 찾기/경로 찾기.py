from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

### 간선이 존재하지 않는 경우의 비용을 무한으로 저장
for row in range(N):
    for col in range(N):
        if graph[row][col] == 0:
            graph[row][col] = INF
     
### 플로이드 워셜 알고리즘 
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
for row in range(N):
    for col in range(N):
        if graph[row][col] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    
    print()