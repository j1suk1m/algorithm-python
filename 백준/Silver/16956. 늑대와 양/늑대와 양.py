from sys import stdin

input = lambda: stdin.readline().rstrip()

def calculate() -> int:
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    for x in range(R):
        for y in range(C):
            if farm[x][y] == "W":
                for dx, dy in zip(dxs, dys):
                    nx = x + dx
                    ny = y + dy

                    if not (0 <= nx < R and 0 <= ny < C): 
                        continue
                    if farm[nx][ny] == "S": ### 늑대와 양이 이웃한 경우
                        return 0
            elif farm[x][y] == ".": ### 모든 빈칸을 울타리로 교체
                farm[x][y] = "D"

    return 1

R, C = map(int, input().split())
farm = list(list(input()) for _ in range(R))

result = calculate()
print(result)

if result:
    for row in farm:
        print("".join(row))