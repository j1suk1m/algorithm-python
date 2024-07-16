from sys import stdin

number1 = int(stdin.readline().rstrip())
number2 = stdin.readline().rstrip()
answer = 0

for i in range(2, -1, -1):
    current_result = number1 * int(number2[i])
    answer += (current_result) * 10 ** (2 - i)
    print(current_result)
    
print(answer)