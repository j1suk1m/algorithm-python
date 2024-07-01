from sys import stdin

N = int(stdin.readline().rstrip())
candies = list(map(int, stdin.readline().rstrip().split()))
odd = 0
result = 0

candies.sort(reverse=True)

for candy in candies:
    if (candy % 2 == 0):
        result += candy
    elif (candy % 2 == 1 and odd > 0):
        result += (candy + odd)
        odd = 0
    else:
        odd = candy
        
print(result)