from sys import stdin

def dynamic_programming(stone: int) -> int:
    dp = [1000] * (stone + 1)
    player = ["SK", "CY"]
    
    dp[1] = 1
    dp[2] = 2
    dp[3] = 1
    
    for turn in range(4, stone + 1):
        dp[turn] = min(dp[turn - 1], dp[turn - 3]) + 1
        
    return player[dp[stone] % 2]
            
N = int(stdin.readline().rstrip())

if N == 1 or N == 3:
    print("CY")
elif N == 2:
    print("SK")
else:
    print(dynamic_programming(N))