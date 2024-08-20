from sys import stdin

input = lambda: stdin.readline().rstrip()

N, K = map(int, input().split())
coins = sorted(list(int(input()) for _ in range(N)), reverse=True)
answer = 0

for coin in coins:
    if coin > K:
        continue
    elif K == 0:
        break
    else:
        answer += K // coin
        K %= coin
        
print(answer)