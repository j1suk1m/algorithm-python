from sys import stdin
from itertools import combinations

heights = [int(stdin.readline().rstrip()) for _ in range(9)]

for dwarfs in list(combinations(heights, 7)):
    if sum(dwarfs) == 100:
        dwarfs = sorted(dwarfs)
        
        for dwarf in dwarfs:
            print(dwarf)
            
        break