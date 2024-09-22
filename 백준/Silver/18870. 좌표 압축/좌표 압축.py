from sys import stdin

input = lambda: stdin.readline().rstrip()

def binary_search(target, start, end):
    while start + 1 < end:
        mid = (start + end) // 2
        
        if compressed_X[mid] == target:
            return mid
        elif compressed_X[mid] > target:
            end = mid
        else:
            start = mid
            
N = int(input())
X = list(map(int, input().split()))
compressed_X = sorted(set(X))

for x in X:
    print(binary_search(x, -1, len(compressed_X)), end=" ")