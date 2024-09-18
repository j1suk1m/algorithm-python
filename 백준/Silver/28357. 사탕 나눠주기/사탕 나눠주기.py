from sys import stdin

input = lambda: stdin.readline().rstrip()

def binary_search(maximum, scores, start, end):    
    answer = 1e12 + 1
        
    while start <= end:
        mid = (start + end) // 2
        total = sum(max(0, score - mid) for score in scores)
        
        if total == maximum:
            answer = mid
            break
        elif total < maximum:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
            
    return answer

N, K = map(int, input().split())
scores = sorted(list(map(int, input().split())))

print(binary_search(K, scores, 0, scores[-1]))