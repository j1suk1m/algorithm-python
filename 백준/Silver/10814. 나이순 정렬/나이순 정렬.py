from sys import stdin

N = int(stdin.readline().rstrip())
members = list(tuple(map(str, stdin.readline().rstrip().split())) + (order, ) for order in range(N)) ### (나이, 이름, 순서)의 리스트
members = sorted(members, key=lambda member: (int(member[0]), member[2]))

for member in members:
    print(member[0], member[1])