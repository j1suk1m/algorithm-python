from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())

if K == 1:
    print(1)
elif K == 2 and N % 2 == 0:
    print(2)
else:
    for divisor in range(1, N + 1):
        if N % divisor == 0:
            K -= 1
        if K == 0:
            print(divisor)
            break
    
    if K != 0:
        print(0)