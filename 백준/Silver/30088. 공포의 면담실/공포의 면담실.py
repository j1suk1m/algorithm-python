from sys import stdin

N = int(stdin.readline().rstrip())
result = 0
time_list = []

for _ in range(N):
    employee = list(map(int, stdin.readline().rstrip().split()))
    time_list.append(sum(employee[1:]))
    
time_list.sort()

for time in time_list:
    result += (time * N)
    N -= 1
    
print(result)