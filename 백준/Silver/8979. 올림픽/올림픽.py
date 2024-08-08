from sys import stdin

N, K = map(int, stdin.readline().rstrip().split())
countries = list(tuple(map(int, stdin.readline().rstrip().split())) for _ in range(N))
countries = sorted(countries, key=lambda country: (-country[1], -country[2], -country[3])) ### 메달에 따라 내림차순 정렬

for i in range(N):
    if countries[i][0] == K: ### 등수를 알고자 하는 국가의 번호
        gold = countries[i][1]
        silver = countries[i][2]
        bronze = countries[i][3]
        
        target_idx = i - 1
        
        for j in range(i - 1, -1, -1):
            target_gold = countries[j][1]
            target_silver = countries[j][2]
            target_bronze = countries[j][3]
            
            if (gold < target_gold or (gold == target_gold and silver < target_silver) 
                or (gold == target_gold and silver == target_silver and bronze < target_bronze)):
                target_idx = j ### K 국가보다 등수가 높은 국가 중 가장 등수가 낮은 국가의 인덱스
                break
            
        print(target_idx + 2)
        break