from sys import stdin

def binary_search(target, numbers):
    start = 0
    end = N - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if numbers[mid] == target:
            return 1
        elif numbers[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return 0

N = int(stdin.readline().rstrip())
numbers = sorted(list(map(int, stdin.readline().rstrip().split())))
M = int(stdin.readline().rstrip())
targets = list(map(int, stdin.readline().rstrip().split()))

for target in targets:
    print(binary_search(target, numbers), end=" ")