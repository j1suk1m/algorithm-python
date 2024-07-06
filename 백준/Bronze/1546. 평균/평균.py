from sys import stdin

N = int(stdin.readline().rstrip())
score_list = list(map(int, stdin.readline().rstrip().split()))

original_average = sum(score_list) / len(score_list)
print(original_average / max(score_list) * 100)