from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
ropes = sorted(list(int(input()) for _ in range(N)), reverse=True)
maximum_weight = 0 ### 각 로프가 버틸 수 있는 최대 중량
count = 0 ### 사용한 로프의 개수

for rope in ropes:
    count += 1
    current_weight = rope * count
    
    if current_weight > maximum_weight:
        maximum_weight = current_weight
        
print(maximum_weight)