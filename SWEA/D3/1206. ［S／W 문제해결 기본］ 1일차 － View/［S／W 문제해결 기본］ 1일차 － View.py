### 조망권이 확보된 세대의 개수를 계산하는 함수
def calculate(heights: list, N: int) -> int:
    result = 0 ### 조망권이 확보된 세대의 개수
    
    for idx in range(2, N - 2):
        current_height = heights[idx]
        max_neighbor_height = max(heights[idx - 2], heights[idx - 1], heights[idx + 1], heights[idx + 2])
        
        if current_height > max_neighbor_height: ### 조망권 확보
            result += (current_height - max_neighbor_height)
            
    return result

T = 10 ### 테스트 케이스 개수
results = [] ### 각 테스트 케이스의 calculate() 실행 결과
    
for _ in range(T):
    N = int(input().rstrip())
    heights = list(map(int, input().rstrip().split()))
    result = calculate(heights, N)
    results.append(result)
    
for test_case in range(T):
    print("#{} {}".format(test_case + 1, results[test_case]))