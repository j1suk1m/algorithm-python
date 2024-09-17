from sys import stdin

input = lambda: stdin.readline().rstrip()

def binary_search(target, budgets, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = sum([min(mid, budget) for budget in budgets])
        
        if total <= target:
            start = mid + 1
        else:
            end = mid - 1
            
    return end

N = int(input())
budgets = sorted(list(map(int, input().split())))
M = int(input())

print(binary_search(M, budgets, 1, budgets[-1]))