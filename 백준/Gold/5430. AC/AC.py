from sys import stdin
from collections import deque

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    P = input()
    N = int(input())
    array = input().strip("[]")
    R_count = 0
    has_error = False
    
    if array == "": ### 빈 정수 배열
        number_deque = deque()
    elif "," not in array: ### 정수가 하나인 배열
        number_deque = deque([int(array)])
    else: ### 정수가 두 개 이상인 배열
        number_deque = deque(array.split(","))
        
    for operation in P:
        try:
            if operation == "R":
                R_count += 1
            elif R_count % 2:
                number_deque.pop()
            else:
                number_deque.popleft()
        except:
            has_error = True
            break
    
    if has_error:
        print("error")        
    else: 
        length = len(number_deque)
        
        if length == 0:
            print("[]")
        elif length == 1:
            print("[" + str(number_deque[0]) + "]")
        else:
            if R_count % 2:
                number_deque.reverse()

            print("[", end="")
            print(",".join(number_deque), end="")
            print("]")