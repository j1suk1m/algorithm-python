from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 노드 번호
### 출력: 해당 노드의 루트 노드 번호
def find_root(node: int) -> int:
    if root[node] != node:
        root[node] = find_root(root[node])
        
    return root[node]

N, M = map(int, input().split())
s, e = map(int, input().split())
graph = []
root = [node for node in range(N + 1)]
answer = int(1e7)
is_solved = False

### 연결 관계 저장
for _ in range(M):
    h1, h2, k = map(int, input().split())
    graph.append((h1, h2, k))

### 무게에 대하여 내림차순 정렬      
graph = sorted(graph, key=lambda x: -x[2])

for node1, node2, cost in graph:
    root1 = find_root(node1)
    root2 = find_root(node2)
    
    if root1 == root2: ### 사이클 발견
        continue
    elif root1 < root2:
        root[root2] = root1
    else:
        root[root1] = root2
        
    answer = min(answer, cost)

    if find_root(s) == find_root(e):
        print(answer)
        is_solved = True
        break
        
if not is_solved:
    print(0)