from sys import stdin

N = int(stdin.readline().rstrip())
result = N
count = 0

while True:
    result = (result % 10) * 10 + (result // 10 + result % 10) % 10
    count += 1
    
    if (result == N):
        break

print(count)