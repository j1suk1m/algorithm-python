from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
sequence = sorted(list(map(int, input().split())))
X = int(input())

left = 0
right = N - 1
count = 0

while left < right:
    sum_of_pair = sequence[left] + sequence[right]
    
    if sum_of_pair > X:
        right -= 1
    else:
        if sum_of_pair == X:
            count += 1
            
        left += 1

print(count)