from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

input = lambda: stdin.readline().rstrip()

def find_root(node: int) -> int:
    if root[node] != node:
        root[node] = find_root(root[node])
        
    return root[node]

N, M = map(int, input().split())
root = [node for node in range(N + 1)]

for _ in range(M):
    operation, a, b = map(int, input().split())
    
    if a == b:
        if operation == 0:
            continue
        else:
            print("YES")
    else:
        root_of_a = find_root(a)
        root_of_b = find_root(b)
        
        if operation == 1:
            if root_of_a == root_of_b:
                print("YES")
            else:
                print("NO")
        elif root_of_a < root_of_b:
            root[root_of_b] = root_of_a
        elif root_of_a > root_of_b:
            root[root_of_a] = root_of_b