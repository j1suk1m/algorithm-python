from sys import stdin
from collections import Counter

angle_1 = int(stdin.readline().rstrip())
angle_2 = int(stdin.readline().rstrip())
angle_3 = int(stdin.readline().rstrip())

if sum((angle_1, angle_2, angle_3)) != 180:
    print("Error")
else:
    counter = Counter((angle_1, angle_2, angle_3))
    same_count = counter.most_common()[0][1]
    
    if same_count == 3:
        print("Equilateral")
    elif same_count == 2:
        print("Isosceles")
    else:
        print("Scalene")