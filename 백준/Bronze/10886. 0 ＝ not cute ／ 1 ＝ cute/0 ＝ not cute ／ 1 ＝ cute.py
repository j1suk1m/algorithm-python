from sys import stdin

N = int(stdin.readline().rstrip())
result = 0

for _ in range(N):
    opinion = int(stdin.readline().rstrip())
    
    if (opinion):
        result += 1
    else:
        result -= 1

if (result > 0):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")