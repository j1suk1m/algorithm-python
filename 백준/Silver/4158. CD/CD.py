from sys import stdin

def binary_search(cd_list, target):
    start = 0
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if cd_list[mid] == target:
            return 1
        elif cd_list[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
            
    return 0

while True:
    N, M = map(int, stdin.readline().rstrip().split())
    
    if N == 0 and M == 0:
        break
    
    answer = 0
    cd_list = sorted(list(int(stdin.readline().rstrip()) for _ in range(N)))
    targets = list(int(stdin.readline().rstrip()) for _ in range(M))
    
    for target in targets:
        answer += binary_search(cd_list, target)
        
    print(answer)