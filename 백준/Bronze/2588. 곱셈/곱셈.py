from sys import stdin

number1 = int(stdin.readline().rstrip())
number2 = stdin.readline().rstrip()

for i in range(2, -1, -1):
    print(number1 * int(number2[i]))
    
print(number1 * int(number2))