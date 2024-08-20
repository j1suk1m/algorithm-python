from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
J = int(input())
positions = [int(input()) for _ in range(J)]
start = 1 ### 바구니의 시작 칸이 가리키는 스크린 숫자
end = M ### 바구니의 끝 칸이 가리키는 스크린 숫자
answer = 0 ### 바구니의 최소 이동 거리

for position in positions:
    if start <= position <= end:
        continue
    elif position < start:
        move = start - position
        answer += move
        start = position
        end -= move
    elif end < position:
        move = position - end
        answer += move
        start += move
        end = position
        
print(answer)