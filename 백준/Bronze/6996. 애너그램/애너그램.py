### 두 단어를 각각 정렬한 결과가 같다면 한쪽의 알파벳 순서를 바꿔서 다른 쪽 단어를 만들 수 있음

from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    A, B = map(str, stdin.readline().rstrip().split())
    
    print(A, "&", B, "are", end=" ")
    
    if sorted(A) != sorted(B):
        print("NOT", end=" ")
        
    print("anagrams.")