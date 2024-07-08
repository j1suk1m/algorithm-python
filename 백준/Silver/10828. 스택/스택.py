from sys import stdin
    
stack = []
N = int(stdin.readline().rstrip())

for _ in range(N):
    operation = list(stdin.readline().rstrip().split())
    
    if (operation[0] == "push"):
        stack.append(operation[1])
    elif (operation[0] == "pop"):
        if (len(stack) == 0):
            print("-1")
        else:
            print(stack.pop())
    elif (operation[0] == "size"):
        print(len(stack))
    elif (operation[0] == "empty"):
        if (len(stack) == 0):
            print("1")
        else:
            print("0")
    else:
        if (len(stack) == 0):
            print("-1")
        else:
            print(stack[-1])