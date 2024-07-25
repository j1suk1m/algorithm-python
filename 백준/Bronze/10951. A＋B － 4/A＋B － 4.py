from sys import stdin

while True:
    numbers = stdin.readline().rstrip()
    
    if numbers == "":
        break
    else:
        A, B = map(int, numbers.split())
        print(A + B)