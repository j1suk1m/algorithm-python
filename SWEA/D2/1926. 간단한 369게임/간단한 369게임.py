N = int(input())

for number in range(1, N + 1):
    count = sum(str(number).count(digit) for digit in "369")
    
    if count > 0:
        print("-" * count, end=" ") 
    else:
        print(number, end=" ")