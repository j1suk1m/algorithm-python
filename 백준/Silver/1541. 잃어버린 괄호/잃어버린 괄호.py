from sys import stdin
from re import findall

input = lambda: stdin.readline().rstrip()

expression = input()
numbers = list(map(int, findall(r"[0-9]+", expression)))
operators = findall(r"[+-]", expression)
has_minus = False
result = numbers[0]

for idx in range(len(operators)):
    operator = operators[idx]
    
    if not has_minus and operator == "+":
        result += numbers[idx + 1]
    else:
        if not has_minus and operator == "-":
            has_minus = True
            
        result -= numbers[idx + 1]

print(result)