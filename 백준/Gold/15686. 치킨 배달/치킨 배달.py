from sys import stdin
from itertools import combinations

input = lambda: stdin.readline().rstrip()

### 각 집마다 치킨 거리 계산
def calculate_chicken_distance(candidate, x, y):
    chicken_distance = int(1e9)

    ### 가장 가까운 치킨집과의 치킨 거리 계산
    for candidate_x, candidate_y in candidate:
        temp = abs(candidate_x - x) + abs(candidate_y - y)
        chicken_distance = min(chicken_distance, temp)

    return chicken_distance

### 입력
N, M = map(int, input().split())
city = list(list(map(int, input().split())) for _ in range(N))

house, chicken_store = 1, 2
city_chicken_distance = int(1e9)
houses = [(x, y) for x in range(N) for y in range(N) if city[x][y] == house]
chicken_stores = [(x, y) for x in range(N) for y in range(N) if city[x][y] == chicken_store]

### 조합을 이용한 후보 치킨집 선정
candidates = list(combinations(chicken_stores, M))

### 각 후보 치킨집마다 도시의 치킨 거리 계산
for candidate in candidates:
    temp = 0

    for x, y in houses:
        temp += calculate_chicken_distance(candidate, x, y)

    ### 도시의 치킨 거리 최솟값 갱신
    city_chicken_distance = min(city_chicken_distance, temp)

### 출력
print(city_chicken_distance)