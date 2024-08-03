from sys import stdin

N = int(stdin.readline().rstrip())
P = sorted(list(map(int, stdin.readline().rstrip().split())))
total_time = 0

for time in P:
    total_time += (time * N)
    N -= 1
    
print(total_time)