from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking(count: int):
    if count == N:
        print(*permutation)
        return
    
    for number in range(1, N + 1):
        if number not in permutation:
            permutation[count] = number
            back_tracking(count + 1)
            permutation[count] = 0
        
N = int(input())
permutation = [0] * N

back_tracking(0)