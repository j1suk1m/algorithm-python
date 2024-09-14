from sys import stdin

input = lambda: stdin.readline().rstrip()

### 백트래킹 알고리즘
def back_tracking(count: int):
    if count == M:
        sequence = list(map(lambda index: numbers[index], sequence_indexes))
        print(*sequence)
        return
    
    ### 중복 수열 제거
    previous = 0
    
    for index in range(N):
        current = numbers[index]
        
        if (index not in sequence_indexes and current != previous and 
            (count == 0 or numbers[sequence_indexes[count - 1]] <= current)):
            previous = current
            sequence_indexes[count] = index
            back_tracking(count + 1)
            sequence_indexes[count] = -1

            
N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
sequence_indexes = [-1] * M

back_tracking(0)