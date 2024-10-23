from sys import stdin

input = lambda: stdin.readline().rstrip()

### 투 포인터 알고리즘
def two_pointers(numbers: list) -> list:
    left, right = 0, len(numbers) - 1
    temp = 2 * (10 ** 9) + 1 ### 0에 가장 가까운 합의 절댓값
    pair = [0, 0]
    
    while left < right:
        sum_of_pair = numbers[left] + numbers[right]
        
        if abs(sum_of_pair) < temp:
            temp = abs(sum_of_pair)
            pair = [numbers[left], numbers[right]]
        
        if sum_of_pair > 0:
            right -= 1
        else:
            left += 1
            
    return pair
    
N = int(input())
numbers = sorted(list(map(int, input().split())))
print(*two_pointers(numbers))