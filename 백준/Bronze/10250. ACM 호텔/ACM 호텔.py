from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    H, W, N = map(int, stdin.readline().rstrip().split())
    
    floor_number = N % H
    room_number = (N - 1) // H + 1
    
    if (floor_number == 0):
        floor_number = H
    
    print(str(floor_number) + str(room_number).zfill(2))