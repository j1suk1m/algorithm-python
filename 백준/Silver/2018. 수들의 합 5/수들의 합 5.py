from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
start = 1
end = 1
current_sum = 1
count = 1

while end < N:
    if current_sum > N:
        current_sum -= start
        start += 1
    else:
        if current_sum == N:
            count += 1
            
        end += 1
        current_sum += end
        
print(count)