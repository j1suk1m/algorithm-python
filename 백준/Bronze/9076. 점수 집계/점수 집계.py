from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    scores = sorted(list(map(int, stdin.readline().rstrip().split())), reverse=True)

    if scores[1] - scores[3] >= 4:
        print('KIN')
    else:
        print(sum(scores[1:4]))