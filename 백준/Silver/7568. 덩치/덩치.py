from sys import stdin

N = int(stdin.readline().rstrip())
build_list = []

for _ in range(N):
    x, y = map(int, stdin.readline().rstrip().split())
    build_list.append([x, y, N])
    
for i in range(N):
    ix = build_list[i][0]
    iy = build_list[i][1]
    
    for j in range(N):   
        jx = build_list[j][0]
        jy = build_list[j][1]
        
        if (i == j or (ix < jx and iy < jy)):
            continue
        else:
            build_list[i][2] -= 1
            
for build in build_list:
    print(build[2], end=" ")