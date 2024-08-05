from sys import stdin

def binary_search(target, heights, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = sum(max(height - mid, 0) for height in heights)

        if total < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
            
    return answer

N, M = map(int, stdin.readline().rstrip().split())
heights = list(map(int, stdin.readline().rstrip().split()))

print(binary_search(M, heights, 0, max(heights)))