from sys import stdin

input = lambda: stdin.readline().rstrip()

### 전위 순회
def preorder_traversal(node: str):
    if node != ".":
        left_child, right_child = tree[node]
        print(node, end="")
        preorder_traversal(left_child)
        preorder_traversal(right_child)

### 중위 순회
def inorder_traversal(node: str):
    if node != ".":
        left_child, right_child = tree[node]
        inorder_traversal(left_child)
        print(node, end="")
        inorder_traversal(right_child)

### 후위 순회
def postorder_traversal(node: str):
    if node != ".":
        left_child, right_child = tree[node]
        postorder_traversal(left_child)
        postorder_traversal(right_child)
        print(node, end="")
    
N = int(input())
tree = {}

for _ in range(N):
    node, left_child, right_child = map(str, input().split())
    tree[node] = [left_child, right_child]
    
preorder_traversal("A")
print()
inorder_traversal("A")
print()
postorder_traversal("A")