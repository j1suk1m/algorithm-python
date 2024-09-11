from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking():
    if len(answer) == M:
        print(*answer)
        return
    
    for number in range(1, N + 1):
        if (len(answer) == 0 or 
            (number > answer[-1] and number not in answer)):
            answer.append(number)
            back_tracking()
            answer.pop()
    
N, M = map(int, input().split())
answer = []

back_tracking()