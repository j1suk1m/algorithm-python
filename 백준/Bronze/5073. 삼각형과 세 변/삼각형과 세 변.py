from sys import stdin
from collections import Counter

while True:
    side_1, side_2, side_3 = map(int, stdin.readline().rstrip().split())
    sides = [side_1, side_2, side_3]
    
    if side_1 == 0 and side_2 == 0 and side_3 == 0:
        break
    elif max(sides) >= sum(sides) - max(sides):
        print("Invalid")
    else:
        counter = Counter(sides)
        same_count = counter.most_common()[0][1]
        
        if same_count == 3:
            print("Equilateral")
        elif same_count == 2:
            print("Isosceles")
        else:
            print("Scalene")