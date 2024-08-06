from sys import stdin

def binary_search(target):
    start = 0
    end = target
    
    while start <= end:
        mid = (start + end) // 2
        square_of_mid = mid ** 2
        
        if square_of_mid == target:
            return mid
        elif square_of_mid > target:
            end = mid - 1
        else:
            start = mid + 1
            
N = int(stdin.readline().rstrip())

print(binary_search(N))