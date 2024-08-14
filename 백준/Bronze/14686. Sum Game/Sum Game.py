from sys import stdin

N = int(stdin.readline().rstrip())
swifts = [0] + list(map(int, stdin.readline().rstrip().split()))
semaphores = [0] + list(map(int, stdin.readline().rstrip().split()))
isSame = False 
sum_of_swifts = 0
sum_of_semaphores = 0
answer = 0

for day in range(1, N + 1):
    sum_of_swifts += swifts[day]
    sum_of_semaphores += semaphores[day]
        
    if sum_of_swifts == sum_of_semaphores and day > answer:
        answer = day
        isSame = True
        
if isSame:
    print(answer)
else:
    print(0)