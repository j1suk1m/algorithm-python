from sys import stdin

n = int(stdin.readline().rstrip())
sequence = [0] + list(map(int, stdin.readline().rstrip().split()))

if n == 1:
    print(sequence[1])
else:
    dp = [0] * (n + 1)
    dp[1] = sequence[1]
    
    for number in range(2, n + 1):
            dp[number] = max(dp[number - 1] + sequence[number], sequence[number])
            
    print(max(dp[1:]))