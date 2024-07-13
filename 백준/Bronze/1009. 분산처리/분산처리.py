from sys import stdin
 
T = int(stdin.readline().rstrip())

for _ in range(T):
    a, b = map(int, stdin.readline().rstrip().split())
    number = a
    exponent = 1
    
    while (b > exponent):
        number *= a
        exponent += 1
        
        if (number % 10 == a % 10):
            exponent -= 1
            break
        
    if b % exponent == 0:
        result = a ** exponent % 10
    else:
        result = a ** (b % exponent) % 10
    
    print(result) if result else print("10")