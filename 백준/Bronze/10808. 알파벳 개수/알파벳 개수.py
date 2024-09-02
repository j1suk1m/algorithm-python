from sys import stdin

input = lambda: stdin.readline().rstrip()

S = input()
alphabets = [0] * 26

for alphabet in S:
    index = ord(alphabet) - ord("a")
    alphabets[index] += 1
    
print(*alphabets)