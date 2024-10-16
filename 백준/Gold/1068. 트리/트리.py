from sys import stdin

input = lambda: stdin.readline().rstrip()
    
### 깊이 우선 탐색 알고리즘
def dfs(node: int, remove: bool):
    if not visited[node]:
        ### 방문 처리
        visited[node] = 1 
        
        ### 리프 노드 발견
        if (not remove and 
            len(graph[node]) == sum(list(visited[child] for child in graph[node]))):
            leaf_node_count[0] += 1
            return
        
        ### 자식 노드로 이동
        for next in graph[node]:
            if not visited[next]:
                dfs(next, remove)
            
    return
            
N = int(input())
parents = list(map(int, input().split()))
removed_node = int(input())
graph = [[] for _ in range(N)]
visited = [0] * N
leaf_node_count = [0]
root = 0

for node in range(N):
    parent = parents[node]
    
    if parent == -1:
        root = node
    else:
        graph[parent].append(node)

### 제거될 노드와 그 노드의 모든 자손을 방문 처리    
dfs(removed_node, True)

### 트리 순회
dfs(root, False)

print(leaf_node_count[0])