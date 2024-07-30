from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

def dfs(node):
    visited[node] = 1 ### 방문 처리
    count = 1
    
    for next in graph[node]:
        if not visited[next]:
            count += dfs(next)
            
    return count
    
N, M = map(int, stdin.readline().rstrip().split()) ### 작업의 개수, 작업 순서 정보의 개수
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1) 

for _ in range(M):
    A, B = map(int, stdin.readline().rstrip().split())
    graph[B].append(A) ### 작업 B를 하기 위해서 작업 A가 직전에 선행되어야 함
    
X = int(stdin.readline().rstrip()) ### 오늘 반드시 끝내야 하는 작업

print(dfs(X) - 1) ### X를 제외한 탐색 결과