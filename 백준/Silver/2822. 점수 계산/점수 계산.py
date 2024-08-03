from sys import stdin

scores = list((int(stdin.readline().rstrip()), order) for order in range(1, 9))
scores = sorted(scores, key=lambda score:(-score[0])) ### 점수에 대한 내림차순 정렬
scores = scores[:5] ### 상위 점수 5개 추출

print(sum(list(score[0] for score in scores))) ### 점수의 총합
print(*sorted(list(score[1] for score in scores))) ### 문제 번호에 대한 오름차순 정렬 및 출력