from sys import stdin
 
T = int(stdin.readline().rstrip())

for _ in range(T):
    stdin.readline().rstrip()
    N, M = map(int, stdin.readline().rstrip().split())
    sejun_list = list(map(int, stdin.readline().rstrip().split()))
    sebi_list = list(map(int, stdin.readline().rstrip().split()))
    sejun_idx = 0 ### 가장 약한 병사를 가리키는 인덱스
    sebi_idx = 0 ### 가장 약한 병사를 가리키는 인덱스
    
    sejun_list.sort()
    sebi_list.sort()
    
    while (sejun_idx != N and sebi_idx != M): ### 한 쪽의 병력이 모두 소진될 때까지
        
        sejun_weakest = sejun_list[sejun_idx]
        sebi_weakest = sebi_list[sebi_idx]
        
        if (sejun_weakest < sebi_weakest):
            sejun_idx += 1
        else:
            sebi_idx += 1
    
    if sejun_idx == N:
        print("B")
    elif sebi_idx == M:
        print("S")
    else:
        print("C")