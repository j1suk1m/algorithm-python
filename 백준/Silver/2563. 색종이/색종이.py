from sys import stdin

N = int(stdin.readline().rstrip())
graph = [[0] * (101) for _ in range(101)]
area = 0

for _ in range(N):
    Y, X = map(int, stdin.readline().rstrip().split())
    
    for x in range(X + 1, X + 11):
        for y in range(Y + 1, Y + 11):
            graph[x][y] = 1
            
for row in graph:
    area += sum(row)
        
print(area)