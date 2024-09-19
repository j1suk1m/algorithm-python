from sys import stdin

input = lambda: stdin.readline().rstrip()

def binary_search(lengths, start, end):
    answer = 0
            
    while start <= end:
        mid = (start + end) // 2
        count = sum(length // mid for length in lengths)
        
        if count < M:
            end = mid - 1
        else:
            answer = max(answer, mid)
            start = mid + 1
            
    return answer

M, N = map(int, input().split())
lengths = sorted(list(map(int, input().split())))

print(binary_search(lengths, 1, lengths[-1]))