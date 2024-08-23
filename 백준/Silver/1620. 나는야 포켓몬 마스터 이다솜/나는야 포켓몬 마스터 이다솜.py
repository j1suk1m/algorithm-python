from sys import stdin

input = lambda: stdin.readline().rstrip()

N, M = map(int, input().split())
pocket_dict = dict() ### key: 이름, value: 번호
pocket_list = [0] * (N + 1) ### index: 번호, element: 이름

for number in range(1, N + 1):
    name = input()
    pocket_dict[name] = number
    pocket_list[number] = name
    
for _ in range(M):
    question = input()
    
    if question.isdigit():
        print(pocket_list[int(question)])
    else:
        print(pocket_dict[question])