from sys import stdin

input = lambda: stdin.readline().rstrip()

def monitor():
    for x, y in teacher_coordinates:

        nx, ny = x - 1, y
        while nx >= 0: ### 위쪽 감시
            if graph[nx][ny] == "O":
                break
            elif graph[nx][ny] == "S":
                return False

            nx -= 1

        nx, ny = x + 1, y
        while nx < N: ### 아래쪽 감시
            if graph[nx][ny] == "O":
                break
            elif graph[nx][ny] == "S":
                return False

            nx += 1

        nx, ny = x, y - 1
        while ny >= 0: ### 왼쪽 감시
            if graph[nx][ny] == "O":
                break
            elif graph[nx][ny] == "S":
                return False

            ny -= 1

        nx, ny = x, y + 1
        while ny < N:  ### 오른쪽 감시
            if graph[nx][ny] == "O":
                break
            elif graph[nx][ny] == "S":
                return False

            ny += 1

    return True

def back_tracking(count: int):
    global is_possible

    if count == 3: ### 장애물 3개 세우기 완료
        is_possible = monitor() ### 감시
        
        return is_possible

    for x, y in space_coordinates:
        if graph[x][y] == "X":
            graph[x][y] = "O" ### 장애물 세우기

            if back_tracking(count + 1):
                return True

            graph[x][y] = "X" ### 장애물 허물기

    return False

N = int(input())
graph = list(input().split() for _ in range(N))

space_coordinates = []
teacher_coordinates = []
is_possible = False

for x in range(N):
    for y in range(N):
        if graph[x][y] == "X":
            space_coordinates.append((x, y))
        elif graph[x][y] == "T":
            teacher_coordinates.append((x, y))

back_tracking(0)

if is_possible:
    print("YES")
else:
    print("NO")