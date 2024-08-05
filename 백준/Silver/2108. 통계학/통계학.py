### 최빈값이 여러 개가 있을 경우 두번째로 작은 수를 출력하기 위해서
### Counter의 most_common(2)를 이용해 가장 많이 등장한 상위 2개의 수를 뽑은 뒤
### 두 수의 등장 횟수가 같으면 두번째 수를, 다르면 첫번째 수를 출력

from sys import stdin
from collections import Counter

N = int(stdin.readline().rstrip())
numbers = sorted(list(int(stdin.readline().rstrip()) for _ in range(N)))
counter = Counter(numbers).most_common(2) 

print(int(round(sum(numbers) / N, 0)))
print(numbers[N // 2])
print(counter[0][0] if len(counter) == 1 or counter[0][1] != counter[1][1] else counter[1][0])
print(numbers[N - 1] - numbers[0])