from sys import stdin

input = lambda: stdin.readline().rstrip()

def find_root(node: int) -> int:
    if root[node] != node:
        root[node] = find_root(root[node])
        
    return root[node]

N, M = map(int, input().split())
gender = [""] + input().split()
graph = []
root = [node for node in range(N + 1)]
answer = 0
count = 0

for _ in range(M):
    u, v, d = map(int, input().split())
    
    if gender[u] != gender[v]:
        graph.append((u, v, d))

graph = sorted(graph, key=lambda x: x[2])

for school1, school2, distance in graph:
    root1 = find_root(school1)
    root2 = find_root(school2)
    
    if root1 == root2:
        continue
    elif root1 < root2:
        root[root2] = root1
    else:
        root[root1] = root2
        
    answer += distance
    count += 1
    
if count == N - 1:
    print(answer)
else:
    print(-1)