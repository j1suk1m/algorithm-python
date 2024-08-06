from sys import stdin

def binary_search(target):
    start = 0
    end = target
    answer = -1
    
    while start <= end:
        mid = (start + end) // 2
        square_of_mid = mid ** 2
        
        if square_of_mid >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer

n = int(stdin.readline().rstrip())

print(binary_search(n))