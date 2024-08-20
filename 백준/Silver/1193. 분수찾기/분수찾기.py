from sys import stdin

input = lambda: stdin.readline().rstrip()

X = int(input())
N = 1

while True:
    sum = N * (N + 1) // 2
    
    if sum < X:
        N += 1
    else:
        break

answer = [1, N] ### 분자, 분모

answer[0] += X - (sum - N + 1)
answer[1] -= X - (sum - N + 1)

if N % 2:
    answer.reverse()
    
print("/".join(list(map(str, answer))))