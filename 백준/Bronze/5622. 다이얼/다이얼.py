from sys import stdin

word = stdin.readline().rstrip()
time = [3] * 3 + [4] * 3 + [5] * 3 + [6] * 3 + [7] * 3 + [8] * 4 + [9] * 3 + [10] * 4
result = 0

for alphabet in word:
    result += time[ord(alphabet) - 65]
    
print(result)