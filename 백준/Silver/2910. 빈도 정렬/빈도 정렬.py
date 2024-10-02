from sys import stdin

input = lambda: stdin.readline().rstrip()

N, C = map(int, input().split())
message = list(map(int, input().split()))
frequency = dict()

for index in range(N):
    number = message[index]
    
    if number in frequency.keys():
        frequency[number].append(index)
    else:
        frequency[number] = [index]
        
sorted_frequency = sorted(frequency.items(), key=lambda x: (-len(x[1]), x[1][0]))

for number, indices in sorted_frequency:
    for _ in range(len(indices)):
        print(number, end=" ")