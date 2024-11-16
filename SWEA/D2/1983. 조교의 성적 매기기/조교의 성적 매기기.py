def calculate(score: list, idx: int) -> tuple:
    return score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.2, idx

T = int(input())
grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
results = []

for _ in range(T):
    N, K = map(int, input().split())
    scores = list(list(map(int, input().split())) for _ in range(N))

    total_scores = list(calculate(scores[idx], idx) for idx in range(N))
    sorted_total_scores = sorted(total_scores, key=lambda x: -x[0])

    for rank in range(N):
        if sorted_total_scores[rank][1] + 1 == K:
            results.append(grades[rank // (N // 10)])
            break

for test_case in range(T):
    print("#{} {}".format(test_case + 1, results[test_case]))