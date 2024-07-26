### (일 때 push, )일 때 pop을 한다고 가정
### 올바른 괄호 문자열의 조건은 1. pop을 할 때 IndexError가 발생하지 않음, 2. 문자열 탐색 종료 후 stack이 비어 있음

from sys import stdin
from collections import deque

def isValid(string: str):
    stack = deque()
    
    try:
        for char in string:
            if char == '(':
                stack.append('(')
            else:
                stack.pop()
    except IndexError:
        return False
    else:
        if len(stack) > 0:
            return False
        else:
            return True

T = int(stdin.readline().rstrip())

for _ in range(T):
    string = stdin.readline().rstrip()
    
    if isValid(string):
        print("YES")
    else:
        print("NO")