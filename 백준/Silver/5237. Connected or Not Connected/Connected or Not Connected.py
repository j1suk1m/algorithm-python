from sys import stdin
from collections import deque

def bfs(node):
    queue = deque([node])
    visited[node] = 1 ### 방문 처리
    
    while queue:
        node = queue.popleft()
        
        for next in graph[node]:
            if not visited[next]:
                queue.append(next)
                visited[next] = 1 ### 방문 처리
                
    return sum(visited) == n ### 모든 정점을 방문했는지 확인

T = int(stdin.readline().rstrip()) ### 테스트 케이스의 개수

for _ in range(T):
    test_case = list(map(int, stdin.readline().rstrip().split()))
    n, k = test_case[0], test_case[1]
    graph = [[] for _ in range(n)]
    isConnected = True
    
    for idx in range(2, 2 * k + 1, 2):
        graph[test_case[idx]].append(test_case[idx + 1])
        graph[test_case[idx + 1]].append(test_case[idx])
    
    for number in range(n):
        visited = [0] * n
        
        if not bfs(number):
            isConnected = False
            break
        
    if isConnected:
        print("Connected.")
    else:
        print("Not connected.")