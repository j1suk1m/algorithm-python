from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
price = [0] + list(map(int, input().split()))

if N == 1:
    print(0)
else:
    dp = [[0, 0] for _ in range(N + 1)] ### [현재까지 가능한 최소 주가, 현재까지 가능한 최대 주가] 리스트
    dp[1] = [price[1], price[1]]
    
    for today in range(2, N + 1):
        today_price = price[today] ### 오늘의 주가
        min_price_yesterday = dp[today - 1][0] ### 어제까지의 주가 중 최솟값 

        if today_price < min_price_yesterday:
            dp[today] = [today_price, today_price]
        else:
            dp[today] = [min_price_yesterday, today_price]
            
    dp = sorted(dp, key=lambda x: -(x[1] - x[0]))

    print(dp[0][1] - dp[0][0])