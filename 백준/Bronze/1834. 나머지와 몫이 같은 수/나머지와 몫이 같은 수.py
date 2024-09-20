from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
answer = 0

for number in range(1, N):
    answer += (number * N + number)
    
print(answer)