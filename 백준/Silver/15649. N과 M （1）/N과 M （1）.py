from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking():
    if len(answer) == M:
        print(*answer)
        return
    
    for number in range(1, N + 1):
        if not number in answer:
            answer.append(number)
            back_tracking()
            answer.pop()
    
N, M = map(int, input().split())
answer = []

back_tracking()