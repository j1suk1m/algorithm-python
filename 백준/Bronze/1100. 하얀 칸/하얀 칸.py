from sys import stdin

input = lambda: stdin.readline().rstrip()

board = list(list(input()) for _ in range(8))
answer = 0

for row in range(8):
    for col in range(8):
        if (row + col) % 2 == 0 and board[row][col] == "F":
            answer += 1
            
print(answer) 