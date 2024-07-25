from sys import stdin

letters = []
max_length = 0

for _ in range(5):
    row = list(stdin.readline().rstrip())
    letters.append(row)
    
    if max_length < len(row):
        max_length = len(row)
    
for col in range(max_length):
    for row in range(5):
        if col < len(letters[row]):
            print(letters[row][col], end="")