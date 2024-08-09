from sys import stdin

def dynamic_programming(apart, floor_num, room_num):
    for floor in range(1, floor_num + 1):
        for room in range(1, room_num + 1):
            apart[floor][room] = apart[floor][room - 1] + apart[floor - 1][room]
            
    return apart[floor_num][room_num]

T = int(stdin.readline().rstrip())

for _ in range(T):
    k = int(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    apart = [[0] * (n + 1) for _ in range(k + 1)]
    
    for room in range(1, n + 1):
        apart[0][room] = room
        
    print(dynamic_programming(apart, k, n))