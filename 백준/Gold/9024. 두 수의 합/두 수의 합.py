from sys import stdin

input = lambda: stdin.readline().rstrip()

### 투 포인터 알고리즘
def two_pointers(numbers: list) -> int:
    left, right = 0, len(numbers) - 1
    temp = 10 ** 9 ### K와 가장 가까운 합
    count_of_pair = 0
    
    while left < right:
        sum_of_pair = numbers[left] + numbers[right]
        
        if abs(sum_of_pair - K) < abs(temp - K):
            count_of_pair = 1
            temp = sum_of_pair
        elif abs(sum_of_pair - K) == abs(temp - K):
            count_of_pair += 1
        
        if sum_of_pair > K:
            right -= 1
        else:
            left += 1
            
    return count_of_pair
    
T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    print(two_pointers(numbers))