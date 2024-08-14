from sys import stdin

S = [0] + list(map(int, list(stdin.readline().rstrip())))
N = len(S) - 1

if N == 2:
    print(2)
else:
    prefix_sum = [0] * (N + 1)
    answer = 0
    isSolved = False
    
    prefix_sum[1] = S[1]
    
    ### 누적 합 저장
    for idx in range(2, N + 1):
        prefix_sum[idx] = prefix_sum[idx - 1] + S[idx]
                
    for length in range(2 * (N // 2), 1, -2):
        for left_start in range(1, N - length + 2):
            left_end = left_start + length // 2 - 1
            right_start = left_end + 1
            right_end = right_start + length // 2 - 1
            
            if (prefix_sum[left_end] - prefix_sum[left_start - 1] ==
                prefix_sum[right_end] - prefix_sum[right_start - 1]):
                answer = length
                isSolved = True
                break
            
        if isSolved:
            break
            
    print(answer)