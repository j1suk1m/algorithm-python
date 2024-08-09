from sys import stdin

def dynamic_programming(numbers: list, length: int, mode: str) -> int:
    dp = [1] * length
    
    for idx in range(1, length):
        if ((mode == "ascending" and numbers[idx] >= numbers[idx - 1]) or 
            (mode == "descending" and numbers[idx] <= numbers[idx - 1])):
            dp[idx] = dp[idx - 1] + 1
            
    return max(dp)

N = int(stdin.readline().rstrip())
numbers = list(map(int, stdin.readline().rstrip().split()))

print(max(dynamic_programming(numbers, N, "ascending"), dynamic_programming(numbers, N, "descending")))