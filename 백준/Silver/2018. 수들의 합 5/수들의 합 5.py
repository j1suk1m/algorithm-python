from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
numbers = [number for number in range(1, N + 1)]
start = 0
end = 0
count = 0

while start <= end:
    prefix_sum = sum(numbers[start:end + 1])
    
    if prefix_sum >= N:
        if prefix_sum == N:
            count += 1
        start += 1
    else:
        end += 1
        
print(count)