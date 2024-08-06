from sys import stdin

def binary_search(target, numbers):
    start = 0
    end = N - 1
    answer = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if numbers[mid] == target:
            answer = mid
            end = mid - 1 ### 처음으로 등장한 것이 맞는지 확인
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return answer

N, M = map(int, stdin.readline().rstrip().split())
A = sorted(list(int(stdin.readline().rstrip()) for _ in range(N)))

for _ in range(M):
    D = int(stdin.readline().rstrip())
    print(binary_search(D, A))