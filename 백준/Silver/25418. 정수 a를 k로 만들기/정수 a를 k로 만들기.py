from sys import stdin
from collections import deque

def bfs(number):
    queue = deque([(number, 0)])
    visited[number] = 1
    
    while queue:
        number, count = queue.popleft()
        
        if number == K:
            return count
        
        for next in [number * 2, number + 1]:
            if next == K:
                return count + 1
            elif (next < K and visited[next] == 0):
                queue.append((next, count + 1))
                visited[next] = 1
                
A, K = map(int, stdin.readline().rstrip().split())
visited = [0] * 1000001

print(bfs(A))