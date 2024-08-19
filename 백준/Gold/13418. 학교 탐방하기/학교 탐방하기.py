from sys import stdin

input = lambda: stdin.readline().rstrip()

def find_root(node: int, root: list) -> int:
    if root[node] != node:
        root[node] = find_root(root[node], root)
        
    return root[node]

def get_fatigue(mode: str, graph: list) -> int:
    if mode == "best":
        graph = sorted(graph, key=lambda x: -(x[2]))
    else:
        graph = sorted(graph, key=lambda x: x[2])
        
    root = [node for node in range(N + 1)]
    count = 0
    
    for node1, node2, road in graph:
        root1 = find_root(node1, root)
        root2 = find_root(node2, root)
        
        if root1 == root2:
            continue
        elif root1 < root2:
            root[root2] = root1
        else:
            root[root1] = root2
            
        count += (1 - road)
        
    return count ** 2

N, M = map(int, input().split())
graph = []

for _ in range(M + 1):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

print(get_fatigue("worst", graph) - get_fatigue("best", graph))