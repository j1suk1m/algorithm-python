from sys import stdin

N = int(stdin.readline().rstrip())
plan_list = list(map(int, stdin.readline().rstrip().split()))
study_list = list(map(int, stdin.readline().rstrip().split()))
count = 0

for (x, y) in zip(plan_list, study_list):
    if (x <= y):
        count += 1

print(count)