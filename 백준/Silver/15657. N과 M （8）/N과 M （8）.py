from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking(count: int):
    if count == M:
        print(*sequence)
        return
    
    for number in numbers:
        if count > 0 and number < sequence[count - 1]:
            continue
        
        sequence[count] = number
        back_tracking(count + 1)
        sequence[count] = 0
    
N, M = map(int, input().split()) 
numbers = sorted(list(map(int, input().split())))
sequence = [0] * M

back_tracking(0)