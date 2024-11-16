from sys import stdin

input = lambda: stdin.readline().rstrip()

def back_tracking(selected_cards: list, count: int):
    if count == K: ### 총 K개의 카드를 선택한 경우
        number = "".join(map(str, selected_cards)) ### 카드로 만들 수 있는 정수
        numbers.add(number) ### 정수 집합에 추가
        return

    for idx in range(len(cards)):
        if not visited[idx]:
            visited[idx] = 1
            back_tracking(selected_cards + [cards[idx]], count + 1)
            visited[idx] = 0

N = int(input())
K = int(input())
cards = list(int(input()) for _ in range(N))

selected_cards = []
visited = [0] * N
numbers = set() ### 중복 제거

back_tracking(selected_cards, 0)

print(len(numbers))