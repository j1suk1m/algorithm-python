### 맨 아랫줄의 정사각형이 n개일 때, 전체 정사각형의 개수는 1부터 n까지의 합인 n(n + 1)/2
### 겹친 부분(T 모양)의 개수는 1부터 n - 1까지의 합인 n(n - 1)/2
### 따라서 전체 둘레는 4 * (n(n + 1)/2) - 4 * (n(n - 1)/2) = 4n

from sys import stdin

n = int(stdin.readline().rstrip())
print(4 * n)