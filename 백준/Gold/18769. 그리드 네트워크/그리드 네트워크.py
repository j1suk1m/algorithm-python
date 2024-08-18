from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 노드 번호
### 출력: 해당 노드의 루트 노드 번호
def find_root(node: int) -> int:
    if root[node] != node:
        root[node] = find_root(root[node])
        
    return root[node]

### 입력: 최대 열의 크기, 행 좌표, 열 좌표
### 출력: 노드 번호
def get_node_number(C: int, row: int, col: int) -> int:
    return C * (row - 1) + col

T = int(input())

for _ in range(T):
    R, C = map(int, input().split())
    graph = []
    root = [node for node in range(R * C + 1)]
    answer = 0 ### 최소 설치 비용의 총합

    ### 좌우 연결 관계 저장
    for row in range(1, R + 1):
        cost = [0] + list(map(int, input().split()))        

        for col in range(1, C):
            graph.append((get_node_number(C, row, col), get_node_number(C, row, col + 1), cost[col]))
    
    ### 상하 연결 관계 저장
    for row in range(1, R):
        cost = [0] + list(map(int, input().split()))
        
        for col in range(1, C + 1):
            graph.append((get_node_number(C, row, col), get_node_number(C, row + 1, col), cost[col]))

    ### 비용에 대한 오름차순 정렬      
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
        
        answer += cost

    print(answer)