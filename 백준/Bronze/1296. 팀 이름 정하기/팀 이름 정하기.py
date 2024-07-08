from sys import stdin
from collections import Counter

name = stdin.readline().rstrip()
N = int(stdin.readline().rstrip())
result_list = []

for _ in range(N):
    team_name = stdin.readline().rstrip()
    counter = Counter(name + team_name)
    L = O = V = E = 0

    if 'L' in counter:
        L = counter['L']
    if 'O' in counter:
        O = counter['O']
    if 'V' in counter:
        V = counter['V']
    if 'E' in counter:
        E = counter['E']
        
    probability = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    result_list.append((probability, team_name))

result_list.sort(key=lambda x:(-x[0], x[1]))

print(result_list[0][1])