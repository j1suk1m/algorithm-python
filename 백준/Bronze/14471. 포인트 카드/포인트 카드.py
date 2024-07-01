N, M = map(int, input().split())
winnings = []
result = 0

for _ in range(M):
    A, B = map(int, input().split())
    winnings.append(A)
    
winnings.sort(reverse=True)

for winning in winnings:
    if (M <= 1):
        break
    elif (winning < N):
        result += (N - winning)
    M -= 1

print(result)