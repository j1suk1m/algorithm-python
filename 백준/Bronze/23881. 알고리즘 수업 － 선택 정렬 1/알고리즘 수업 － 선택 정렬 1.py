from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
A = list(map(int, input().split()))

### 선택 정렬 알고리즘
for i in range(N - 1, 0, -1):
    maximum_number = A[0]
    maximum_number_index = 0
    
    ### 최댓값 찾기
    for j in range(i + 1):
        if A[j] > maximum_number:
            maximum_number = A[j]
            maximum_number_index = j
        
    if i != maximum_number_index:
        A[i], A[maximum_number_index] = A[maximum_number_index], A[i]
        K -= 1
        
        if K == 0:
            print(min(A[i], A[maximum_number_index]), max(A[i], A[maximum_number_index]))
            break
        
if K > 0:
    print("-1")