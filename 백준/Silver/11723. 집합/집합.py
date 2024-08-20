from sys import stdin

input = lambda: stdin.readline().rstrip()

M = int(input())
S = set()

for _ in range(M):
    operations = input().split()
    operation = operations[0]
    
    if operation == "add":
        S.add(int(operations[1]))
    elif operation == "remove":
        S.discard(int(operations[1]))
    elif operation == "check":
        print(1) if int(operations[1]) in S else print(0)
    elif operation == "toggle":
        S ^= set([int(operations[1])])
    elif operation == "all":
        S = set(num for num in range(1, 21))
    else:
        S.clear()