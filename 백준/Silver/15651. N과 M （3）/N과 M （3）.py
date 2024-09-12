from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking(sequence: str):
    if len(sequence) == M:
        sequences.append(sequence)
        print(" ".join(sequence))
        return
    
    for number in range(1, N + 1):
        if (len(sequence) == M - 1 and len(sequences) > 0 and int(sequence + str(number)) <= int(sequences[-1])):
            continue

        back_tracking(sequence + str(number))
    
N, M = map(int, input().split()) 
sequences = []

back_tracking("")