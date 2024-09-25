from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0

if A == B:
    print(1)
else:
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
            
            if A == B:
                answer = 1
                break
            
    print(answer)