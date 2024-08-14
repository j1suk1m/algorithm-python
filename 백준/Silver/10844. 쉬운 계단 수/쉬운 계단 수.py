from sys import stdin

N = int(stdin.readline().rstrip())

if N == 1:
    print(9)
else:
    dp = [[0] * 10 for _ in range(N + 1)] ### 인덱스가 n일 때, n으로 끝나는 계단 수의 개수 리스트
    
    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] 
    
    for length in range(2, N + 1):
        for number in range(10):
            if number == 0:
                dp[length][number] = (dp[length - 1][number + 1]) % 1000000000
            elif number == 9:
                dp[length][number] = (dp[length - 1][number - 1]) % 1000000000
            else:
                dp[length][number] = (dp[length - 1][number - 1] + dp[length - 1][number + 1]) % 1000000000
                
    print(sum(dp[N]) % 1000000000)