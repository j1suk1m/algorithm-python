from sys import stdin

input = lambda: stdin.readline().rstrip()

### 백트래킹 알고리즘
def back_tracking(count: int):
    if count == M:
        sequence = list(map(lambda index: numbers[index], sequence_indexes))
        sequences.append(sequence)
        return
    
    for index in range(N):
        if index not in sequence_indexes:
            sequence_indexes[count] = index
            back_tracking(count + 1)
            sequence_indexes[count] = -1
            
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sequence_indexes = [-1] * M
sequences = []

back_tracking(0)

sequences = sorted(set(tuple(sublist) for sublist in sequences))

for sequence in sequences:
    print(*sequence)