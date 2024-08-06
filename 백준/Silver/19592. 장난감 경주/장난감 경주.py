from sys import stdin

def binary_search(target, velocities):
    start = 1 ### 부스터 사용 시 최솟값
    end = Y ### 부스터 사용 시 최댓값
    rival = max(velocities) ### 경쟁자 중 최대 속도
    answer = -1
    
    while start <= end:
        booster = (start + end) // 2
        
        if (X / rival) > ((X - booster) / target + 1): ### 단독 우승
            answer = booster
            end = booster - 1 ### 부스터 속도를 줄여도 단독 우승이 가능한지 확인
        else: ### 공동 우승 또는 우승 불가
            start = booster + 1 ### 부스터 속도 증가
            
    return answer

T = int(stdin.readline().rstrip())

for _ in range(T):
    N, X, Y = map(int, stdin.readline().rstrip().split())
    velocities = list(map(int, stdin.readline().rstrip().split()))
    target = velocities[N - 1]
    velocities = sorted(velocities)
    
    if target == velocities[N - 1] and target != velocities[N - 2]: ### 부스터를 사용하지 않아도 단독 우승이 가능한 경우
        print(0)
    else:
        print(binary_search(target, velocities))