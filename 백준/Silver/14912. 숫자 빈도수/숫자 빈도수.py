from sys import stdin

input = lambda: stdin.readline().rstrip()

N, D = map(int, input().split())
D = str(D)
answer = 0

for number in range(1, N + 1):
    answer += str(number).count(D)
        
print(answer)