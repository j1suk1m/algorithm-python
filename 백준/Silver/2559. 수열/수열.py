from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
temperatures = list(map(int, input().split()))
prefix_sum = [0] * N

prefix_sum[0] = temperatures[0]

for index in range(1, N):
    prefix_sum[index] = temperatures[index] + prefix_sum[index - 1]
    
answer = prefix_sum[K - 1]

for left in range(1, N - K + 1):
    right = left + K - 1
    answer = max(answer, prefix_sum[right] - prefix_sum[left - 1])
    
print(answer)