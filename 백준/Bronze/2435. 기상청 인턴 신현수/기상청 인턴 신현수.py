from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
array = [0] + list(map(int, stdin.readline().rstrip().split()))

if K == 1:
    print(max(array))
else:
    minimum = -100 ### 가능한 최소 온도
    maximum = minimum * K - 1
    prefix_sum = [0] * (N + 1) ### 누적 합 리스트
    prefix_sum[1] = array[1]
    
    for idx in range(2, N + 1): ### 누적 합 저장
        prefix_sum[idx] = prefix_sum[idx - 1] + array[idx]
        
    for idx in range(K, N + 1): ### 부분 합 계산
        partial_sum = prefix_sum[idx] - prefix_sum[idx - K]
        
        if partial_sum > maximum:
            maximum = partial_sum
            
    print(maximum)