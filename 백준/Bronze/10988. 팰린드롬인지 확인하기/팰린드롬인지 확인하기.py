from sys import stdin
from collections import deque

stack = list(stdin.readline().rstrip())
queue = deque(stack)
isPalindrome = True

while queue:
    if queue.popleft() != stack.pop():
        isPalindrome = False
        break
        
if isPalindrome:
    print(1)
else:
    print(0)