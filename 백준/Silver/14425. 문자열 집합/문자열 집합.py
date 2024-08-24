from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
string_set = set(list(input() for _ in range(N)))
answer = 0

for _ in range(M):
    string = input()
    
    if string in string_set:
        answer += 1
        
print(answer)