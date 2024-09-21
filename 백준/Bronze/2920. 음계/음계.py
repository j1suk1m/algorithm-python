from sys import stdin

input = lambda: stdin.readline().rstrip()

def is_ascending():
    if numbers[0] != 1 or numbers[-1] != 8:
        return False
    
    for index in range(1, len(numbers)):
        if numbers[index] < numbers[index - 1]:
            return False
        
    return True

def is_descending():
    if numbers[0] != 8 or numbers[-1] != 1:
        return False
    
    for index in range(1, len(numbers)):
        if numbers[index] > numbers[index - 1]:
            return False
        
    return True    
        
numbers = list(map(int, input().split()))

if is_ascending():
    print("ascending")
elif is_descending():
    print("descending")
else:
    print("mixed")