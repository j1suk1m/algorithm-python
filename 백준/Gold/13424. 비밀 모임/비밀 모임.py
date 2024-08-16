from sys import stdin

input = lambda: stdin.readline().rstrip()
INF = int(1e9)

### 플로이드 워셜 알고리즘
def floyd_warshall(graph: list, N: int) -> list:
    for k in range(1, N + 1):
        graph[k][k] = 0
        
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                    
    return graph

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    
    ### 연결 관계 저장
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
        
    K = int(input())
    friends = list(map(int, input().split()))
    answer = []
    
    ### 플로이드 워셜 알고리즘
    graph = floyd_warshall(graph, N)
    
    ### 이동 거리의 총합 계산 후 정렬
    for place in range(1, N + 1):
        distance = 0
        
        for friend in friends:
            distance += graph[friend][place]
            
        answer.append((distance, place))
        
    answer = sorted(answer, key=lambda x: (x[0], x[1]))
    print(answer[0][1])