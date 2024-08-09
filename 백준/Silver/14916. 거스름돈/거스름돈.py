from sys import stdin

def dynamic_programming(money: int) -> int:
    coins = [100000] * (money + 1)
    
    for i in range(2, money + 1):
        coins[i] = coins[i - 2] + 1
        
        if i % 5 == 0:
            coins[i] = min(coins[i], i // 5)
        if i % 2 == 0:
            coins[i] = min(coins[i], i // 2)
        if i >= 5:
            coins[i] = min(coins[i], coins[i - 5] + 1)
            
    answer = coins[money] if coins[money] < 100000 else -1
    
    return answer
            
n = int(stdin.readline().rstrip())

print(dynamic_programming(n))