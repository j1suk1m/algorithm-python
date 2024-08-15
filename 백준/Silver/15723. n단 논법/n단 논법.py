from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 알파벳 문자
### 출력: 사전 순서에 따른 인덱스
def get_index(char: str) -> int:
    return ord(char) - 97

N = int(input())
graph = [[0] * 26 for _ in range(26)]

for _ in range(N):
    premise = input().split()
    graph[get_index(premise[0])][get_index(premise[2])] = 1
                
### 플로이드 워셜 알고리즘 
for k in range(26):
    for i in range(26):
        for j in range(26):
            if graph[i][j] == 0 and graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

M = int(input())     

for _ in range(M):
    conclusion = input().split()
    
    if graph[get_index(conclusion[0])][get_index(conclusion[2])] == 1:
        print("T")
    else:
        print("F")