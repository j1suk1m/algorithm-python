from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 대소문자 알파벳
### 출력: 인덱스
def get_index(char: str) -> int:
    ascii_code = ord(char)
    
    if ascii_code < ord("a"):
        return ascii_code - ord("A")
    else:
        return ascii_code - ord("a") + 26
        
### 입력: 인덱스
### 출력: 대소문자 알파벳
def get_alphabet(idx: int) -> str:
    if idx // 26 == 0:
        return chr(idx + ord("A"))
    else:
        return chr(idx + ord("a") - 26)

N = int(input())
graph = [[0] * 52 for _ in range(52)]

### 연결 관계 저장
for _ in range(N):
    P, Q = map(str, input().split(" => "))
    
    if P != Q:
        graph[get_index(P)][get_index(Q)] = 1
    
### 플로이드 워셜 알고리즘
for k in range(52):
    for i in range(52):
        for j in range(52):
            if i != j and graph[i][k] and graph[k][j]:
                graph[i][j] = 1

print(sum([sum(row) for row in graph]))

### 증명 가능한 명제 출력
for row in range(52):
    for col in range(52):
        if graph[row][col] == 1:
            print("{} => {}".format(get_alphabet(row), get_alphabet(col)))