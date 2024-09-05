from sys import stdin

input = lambda: stdin.readline().rstrip()

while True:
    number1, number2 = map(int, input().split())
    
    if number1 == 0 and number2 == 0:
        break
    elif number2 % number1 == 0:
        print("factor")
    elif number1 % number2 == 0:
        print("multiple")
    else:
        print("neither")