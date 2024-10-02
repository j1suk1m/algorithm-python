from sys import stdin

input = lambda: stdin.readline().rstrip()

### 입력: 대문자 알파벳과 숫자로 이루어진 시리얼 번호
### 출력: 시리얼 번호에 포함된 숫자의 합
def sum_numbers(serial_number: str) -> int:
    result = 0
    
    for char in serial_number:
        if char.isdigit():
            result += int(char)
            
    return result
            
N = int(input())

serial_numbers = list(input() for _ in range(N))
sorted_serial_numbers = sorted(serial_numbers, key=lambda x: (len(x), sum_numbers(x), x.lower()))

for serial_number in sorted_serial_numbers:
    print(serial_number)