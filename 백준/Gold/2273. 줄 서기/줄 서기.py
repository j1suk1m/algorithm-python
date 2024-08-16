from sys import stdin

input = lambda: stdin.readline().rstrip()

### 플로이드 워셜 알고리즘
def floyd_warshall(graph: list, N: int) -> list:
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
                    
    return graph

### 사이클 판별 
def has_cycle(graph: list, N: int) -> bool:
    for i in range(1, N + 1):
        if graph[i][i] == 1:
            return True
        
    return False

### 범위 계산
def get_range(graph: list, N: int) -> list:
    answer = []
    
    for i in range(1, N + 1):
        taller = sum(graph[i])
        smaller = sum([graph[j][i] for j in range(1, N + 1)])
        
        if taller + smaller >= N:
            return []
        else:
            answer.append((1 + smaller, N - taller))
            
    return answer

N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]

### 연결 관계 저장
for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1

### 플로이드 워셜 알고리즘    
graph = floyd_warshall(graph, N)

if has_cycle(graph, N):
    print(-1)
else:
    answer = get_range(graph, N)
    
    if answer:
        for range in answer:
            print(*range)
    else:
        print(-1)