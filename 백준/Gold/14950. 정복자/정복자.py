from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 노드 번호
### 출력: 해당 노드의 루트 노드 번호
def find_root(node: int) -> int:
    if root[node] != node:
        root[node] = find_root(root[node])
        
    return root[node]

N, M, t = map(int, input().split())
graph = []
root = [node for node in range(N + 1)]
answer = 0 ### 최소 정복 비용
count = 0 ### 최소 신장 트리의 간선의 개수 

### 연결 관계 저장
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

### 비용에 대하여 오름차순 정렬      
graph = sorted(graph, key=lambda x: x[2])

for node1, node2, cost in graph:
    root1 = find_root(node1)
    root2 = find_root(node2)
    
    if root1 == root2: ### 사이클 발견
        continue
    elif root1 < root2:
        root[root2] = root1
    else:
        root[root1] = root2
        
    count += 1
    answer += (cost + t * (count - 1))

print(answer)