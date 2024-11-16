from itertools import permutations

def solution(k, dungeons):
    answer = -1

    ### 탐험할 던전의 총 개수를 하나씩 줄여가며 탐색
    for count in range(len(dungeons), 0, -1):
        
        ### 현재 탐험 가능한 최대 던전 수가 최적의 해인 경우
        if answer >= count:
            break

        exploration = list(permutations(dungeons, count))

        for fatigue in exploration:
            answer_temp = 0
            k_temp = k

            ### 던전 탐험
            for required, consumed in fatigue:
                if k_temp >= required:
                    answer_temp += 1
                    k_temp -= consumed
                else:
                    break

            ### 탐험 가능한 최대 던전 수 갱신
            if answer < answer_temp:
                answer = answer_temp

    return answer