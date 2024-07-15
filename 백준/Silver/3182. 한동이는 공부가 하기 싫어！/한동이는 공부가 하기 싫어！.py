from sys import stdin

def search(node):
    result = 1
    visited[node] = True
    
    while True:
        next = graph[node]
        
        if visited[next]:
            break
        
        visited[next] = True
        node = next
        result += 1
    
    return result

N = int(stdin.readline().rstrip())
graph = [0] * (N + 1)
maximum = 0
answer_number = 0

for i in range(1, N + 1):
    answer = int(stdin.readline().rstrip())
    graph[i] = answer

for node in range(1, N + 1):
    visited = [False] * (N + 1)
    search_result = search(node)
    
    if search_result > maximum:
        maximum = search_result
        answer_number = node
        
print(answer_number)