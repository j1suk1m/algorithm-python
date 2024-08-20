from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
meeting = list(tuple(list(map(int, input().split()))) for _ in range(N))
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))
before_end = -1
answer = 0

for start, end in meeting:
    if start >= before_end:
        answer += 1
        before_end = end
    
print(answer)