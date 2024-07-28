from sys import stdin

N = int(stdin.readline().rstrip())
number = 0
hasAnswer = False

while number < N:
    sum = number
        
    for digit in str(number):
        sum += int(digit)
        
    if sum == N:
        hasAnswer = True
        break
    
    number += 1
        
if hasAnswer: 
    print(number)
else:
    print(0)