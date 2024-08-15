from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
numbers = [1] * (N + 1)

for number in range(2, N + 1):
    if numbers[number] == 1:
        
        ### 현재 숫자의 배수 지우기
        for multiple in range(number, N + 1, number):
            if numbers[multiple] == 1:
                numbers[multiple] = 0
                K -= 1
                
                if K == 0:
                    print(multiple)
                    break
            
    if K == 0:
        break