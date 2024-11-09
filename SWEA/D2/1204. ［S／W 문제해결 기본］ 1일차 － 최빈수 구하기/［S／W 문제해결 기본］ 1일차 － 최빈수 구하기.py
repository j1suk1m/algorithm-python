results = []
T = int(input().rstrip())

for _ in range(T):
    score_frequency = dict()
    test_case = int(input().rstrip())
    scores = list(map(int, input().rstrip().split()))
    
    for score in scores:
        if score in score_frequency.keys():
            score_frequency[score] += 1
        else:
            score_frequency[score] = 1
            
    sorted_score_frequency = sorted(score_frequency.items(), key=lambda score: (-score[1], -score[0]))
    results.append(sorted_score_frequency[0][0])
    
for test_case in range(T):
    print("#{} {}".format(test_case + 1, results[test_case]))