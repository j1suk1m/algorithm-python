from sys import stdin

def fibonacci(number: int) -> int:
    store = [0] * 10001
    store[1] = 1
    
    for i in range(2, number + 1):
        store[i] = store[i - 1] + store[i - 2]
        
    return store[number]
    
n = int(stdin.readline().rstrip())

if n <= 1:
    print(n)
else:
    print(fibonacci(n))