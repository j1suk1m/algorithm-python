from sys import stdin

def search(node):    
    for i in range(len(graph[node])):
        if graph[node][i] == 'Y':
            visited[i] = 1
            
            for j in range(len(graph[i])):
                if j != node and graph[i][j] == 'Y':
                    visited[j] = 1
                    
    return sum(visited)
    
N = int(stdin.readline().rstrip())
graph = []
count = -1

for _ in range(N):
    graph.append(list(stdin.readline().rstrip()))
    
for i in range(N):
    visited = [0] * N
    search_result = search(i)
    
    if search_result > count:
        count = search_result
        
print(count)