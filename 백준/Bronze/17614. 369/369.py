from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())

if N <= 2:
    print(0)
else:
    answer = 0
    
    for number in range(3, N + 1):
        answer += str(number).count("3")
        answer += str(number).count("6")
        answer += str(number).count("9")
        
    print(answer)