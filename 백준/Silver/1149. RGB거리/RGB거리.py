from sys import stdin

N = int(stdin.readline().rstrip())
cost = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]

for house in range(1, N):
    for color in range(3):
        ### 현재 색을 제외한 색 중 이전 행까지의 비용이 적은 색을 선택한 후 현재 색의 비용을 더함
        cost[house][color] += min(cost[house - 1][(color + 1) % 3], cost[house - 1][(color + 2) % 3])
            
print(min(cost[-1]))