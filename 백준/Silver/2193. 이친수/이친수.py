from sys import stdin

def dynamic_programming(N: int) -> int:
    dp = [[0, 0] for _ in range(N + 1)] ### [0으로 끝나는 이친수의 개수, 1로 끝나는 이친수의 개수]의 리스트
    
    dp[1] = [0, 1]
    dp[2] = [1, 0]

    for number in range(3, N + 1):
        ### 0으로 끝나는 n - 1자리 이친수 -> n자리일 때 0으로도 1로도 끝날 수 있음
        ### 1로 끝나는 n - 1자리 이친수 -> n자리일 때 0으로만 끝날 수 있음
        ### n - 1자리 이친수의 개수 == n자리 이친수 중 0으로 끝나는 것의 개수
        ### n - 1자리 이친수 중 0으로 끝나는 것의 개수 == n자리 이친수 중 1로 끝나는 것의 개수
        dp[number] = [sum(dp[number - 1]), dp[number - 1][0]]
        
    return sum(dp[N])

N = int(stdin.readline().rstrip())

if N <= 2:
    print(1)
else:
    print(dynamic_programming(N))