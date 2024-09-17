from sys import stdin

input = lambda: stdin.readline().rstrip()

def binary_search(target, lengths, start, end):
    while start <= end:
        mid = (start + end) // 2
        count = sum([length // mid for length in lengths])

        if count < target:
            end = mid - 1
        else:
            start = mid + 1
            
    return end

K, N = map(int, input().split())
lengths = sorted(list(int(input()) for _ in range(K)))

print(binary_search(N, lengths, 1, lengths[-1]))