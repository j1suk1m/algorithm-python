from sys import stdin

A, B, C, M = map(int, stdin.readline().rstrip().split())
hour = 24
work = 0
tiredness = 0

while hour > 0:
    if (tiredness + A <= M):
        tiredness += A
        work += B
    else:
        tiredness = max(tiredness - C, 0)
        
    hour -= 1

print(work)