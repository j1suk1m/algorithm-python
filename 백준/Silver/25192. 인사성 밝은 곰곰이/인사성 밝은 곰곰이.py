from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
users = set()
answer = 0

for _ in range(N):
    chat = input()
    
    if chat == "ENTER":
        answer += len(users)
        users.clear()
    else:
        users.add(chat)
        
answer += len(users)
print(answer)