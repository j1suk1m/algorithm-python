from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 노드 번호
### 출력: 해당 노드의 루트 노드 번호
def find_root(node: int) -> int:
    if root[node] != node:
        root[node] = find_root(root[node])
        
    return root[node]

N, M = map(int, input().split())
graph = []
root = [node for node in range(N + 1)]
answer = []

### 연결 관계 저장
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

### 연결 비용에 대하여 오름차순 정렬        
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
        
    answer.append(cost)

print(sum(answer) - max(answer))