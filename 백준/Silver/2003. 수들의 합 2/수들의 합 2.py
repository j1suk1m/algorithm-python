from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
A = [0] + list(map(int, stdin.readline().rstrip().split()))
prefix_sum = [0] * (N + 1)
answer = 0

prefix_sum[1] = A[1]

### 누적 합 저장
for idx in range(2, N + 1):
    prefix_sum[idx] = prefix_sum[idx - 1] + A[idx]
    
for length in range(1, N + 1):
    for start in range(1, N - length + 2):
        end = start + length - 1
        
        if prefix_sum[end] - prefix_sum[start - 1] == M:
            answer += 1
        
print(answer)