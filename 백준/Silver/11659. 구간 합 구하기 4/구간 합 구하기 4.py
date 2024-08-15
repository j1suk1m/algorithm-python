from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
prefix_sum = [0] * (N + 1)

prefix_sum[1] = numbers[1]

### 누적 합
for idx in range(2, N + 1):
    prefix_sum[idx] = prefix_sum[idx - 1] + numbers[idx]

### 구간 합
for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])