from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
waiting_list = list(map(int, stdin.readline().rstrip().split()))
friends_list = list(map(int, stdin.readline().rstrip().split()))
result = 0

for friend in friends_list:
    if (waiting_list.index(friend) >= M):
        result += 1

print(result)