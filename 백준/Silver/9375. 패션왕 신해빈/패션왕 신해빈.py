from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    garb_dict = dict()
    answer = 1
    
    for _ in range(N):
        garb, type = map(str, input().split())
        
        if type in garb_dict.keys():
            garb_dict[type] += 1
        else:
            garb_dict[type] = 1
            
    for count in garb_dict.values():
        answer *= (count + 1)
        
    print(answer - 1)