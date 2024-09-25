from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
A = list(map(int, input().split()))

### 버블 정렬 알고리즘
for i in range(N - 1, 0, -1):
    for j in range(i):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            K -= 1
            
            if K == 0:
                print(min(A[j], A[j + 1]), max(A[j], A[j + 1]))
                break
            
    if K == 0:
        break
        
if K > 0:
    print("-1")