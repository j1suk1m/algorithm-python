from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 숫자
### 출력: 리스트의 모든 숫자와의 차이의 총합
def calculate(current_number: int) -> int:
    answer = 0
    
    for number in numbers:
        answer += abs(current_number - number)
        
    return answer

N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers, key=lambda number: (calculate(number), number))

print(sorted_numbers[0])