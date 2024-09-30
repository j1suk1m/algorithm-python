from sys import stdin

input = lambda: stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    boxes = list(tuple(list(map(int, input().split()))) for _ in range(N))
    sorted_boxes = sorted(boxes, key=lambda box: -(box[0] * box[1]))
    count = 0
    
    for R, C in sorted_boxes:
        J -= (R * C)
        count += 1
        
        if J <= 0:
            break
        
    print(count)