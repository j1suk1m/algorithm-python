from sys import stdin

input = lambda: stdin.readline().rstrip()

def power(base: int, exponent: int, mod: int) -> int:
    if exponent == 1:
        return base
    else:
        square_root = power(base, exponent // 2, mod)
        
        if exponent % 2 == 1:
            return (square_root * square_root * base) % mod
        else:
            return (square_root * square_root) % mod 

A, B, C = map(int, input().split())

print(power(A, B, C) % C)