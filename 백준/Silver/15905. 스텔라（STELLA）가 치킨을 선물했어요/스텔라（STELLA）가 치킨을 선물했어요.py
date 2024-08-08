from sys import stdin

N = int(stdin.readline().rstrip())
scores = list(tuple(map(int, stdin.readline().rstrip().split())) for _ in range(N))

if N == 5:
    print(0)
else:
    scores = sorted(scores, key=lambda score: (-score[0], score[1]))
    num_of_problems = scores[4][0] ### 5등이 해결한 문제의 개수
    sum_of_penalties = scores[4][1] ### 5등의 패널티 총합
    print(len(list(score for score in scores if score[0] == num_of_problems and score[1] > sum_of_penalties)))