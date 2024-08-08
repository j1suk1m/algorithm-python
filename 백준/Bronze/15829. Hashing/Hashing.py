from sys import stdin

L = int(stdin.readline().rstrip())
string = stdin.readline().rstrip()
answer = 0

for idx in range(L):
    order = ord(string[idx]) - 96
    answer += (order * (31 ** idx))
    
print(answer % 1234567891)