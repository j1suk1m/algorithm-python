from sys import stdin, setrecursionlimit

input = lambda: stdin.readline().rstrip()
setrecursionlimit(10**6)

### 입력: 노드 번호
### 출력: 해당 노드의 루트 노드 번호
def find_root(node: int) -> int:
    if root[node] != node:
        root[node] = find_root(root[node])
        
    return root[node]

N, Q = map(int, input().split())
graph = []
root = [node for node in range(0, N + 1)]
answer = [0, 0] ### 연합 시각, 최소 건설 비용의 총합
count = 0

### 연결 관계 저장
for _ in range(Q):
    city1, city2, cost, time = map(int, input().split())
    graph.append((city1, city2, cost, time))

### 비용 1순위, 시각 2순위에 대한 오름차순 정렬    
graph = sorted(graph, key=lambda x: (x[2], x[3]))

for city1, city2, cost, time in graph:
    root1 = find_root(city1)
    root2 = find_root(city2)
    
    if root1 == root2: ### 사이클 존재
        continue 
    elif root1 < root2:
        root[root2] = root1
    else:
        root[root1] = root2
        
    answer[0] = max(answer[0], time)
    answer[1] += cost
    count += 1
    
if count == N - 1:
    print(*answer)
else:
    print(-1)