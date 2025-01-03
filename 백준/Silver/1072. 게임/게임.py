from sys import stdin

def binary_search(Z):
    start = 1
    end = X
    answer = -1
    
    while start <= end:
        mid = (start + end) // 2
        
        if (Y + mid) * 100 // (X + mid) > Z: ### 승률 비교
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
    
X, Y = map(int, stdin.readline().rstrip().split())
Z = (Y * 100) // X ### 현재 승률
    
if Z >= 99: ### 추가 게임을 하더라도 승률이 변하지 않는 경우
    print(-1)
else:
    print(binary_search(Z))