from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking(sequence: str):
    if len(sequence) == M:
        print(" ".join(sequence))
        return
    
    for number in range(1, N + 1):
        back_tracking(sequence + str(number))
    
N, M = map(int, input().split()) 

back_tracking("")