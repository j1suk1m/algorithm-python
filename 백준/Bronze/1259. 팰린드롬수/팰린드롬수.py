from sys import stdin
from collections import deque

while True:
    isPalindrome = True
    number = stdin.readline().rstrip()
    
    if (number == '0'):
        break
    else:
        stack = deque(list(number))
        queue = deque(list(number))
        
        while len(stack) > 1:
            if (stack.pop() != queue.popleft()):
                isPalindrome = False
                break
    
    if (isPalindrome):
        print("yes")
    else:
        print("no")