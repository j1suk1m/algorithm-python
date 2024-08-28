from sys import stdin

input = lambda: stdin.readline().rstrip()

A, B = map(int, input().split())
answer = A * B

while B > 0:
    A, B = B, A % B
    
### 두 수의 최소 공배수는 두 수의 곱 나누기 두 수의 최대 공약수
print(answer // A) 