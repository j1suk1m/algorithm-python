from sys import stdin
from collections import deque

def isValid(string: str):
    stack = deque() 
    
    try:
        for char in string:
            if char == '(' or char == '[':
                stack.append(char)
            elif char == ')':
                if stack.pop() != '(':
                    return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
            else:
                continue
    except:
        return False
    else:
        if len(stack) > 0 :
            return False
        else:
            return True

while True:
    string = stdin.readline().rstrip()
    
    if string == '.':
        break
    elif isValid(string):
        print("yes")
    else:
        print("no")