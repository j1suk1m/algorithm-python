from sys import stdin

H, M = map(int, stdin.readline().rstrip().split())

if (M < 45):
    if (H == 0):
        H = 23
    else:
        H -= 1
        
    M = (M + 60) - 45

else:
    M -= 45
    
print(H, M)