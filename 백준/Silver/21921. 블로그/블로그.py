from sys import stdin

input = lambda: stdin.readline().rstrip()

N, X = map(int, input().split())
visitor = list(map(int, input().split()))

if sum(visitor) == 0:
    print("SAD")
else:
    prefix_sum = [0] * (N - X + 1)
    idx = 0

    prefix_sum[0] = sum(visitor[:X])

    ### 슬라이딩 윈도우 알고리즘
    for start in range(1, N - X + 1):
        end = start + X - 1
        prefix_sum[start] = prefix_sum[start - 1] + visitor[end] - visitor[start - 1]
        
    prefix_sum = sorted(prefix_sum, reverse=True)
    maximum = prefix_sum[0]

    while idx < len(prefix_sum) and prefix_sum[idx] == maximum:
        idx += 1
        
    print(maximum)
    print(idx)