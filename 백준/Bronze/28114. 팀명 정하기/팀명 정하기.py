from sys import stdin

team = list(list(map(str, stdin.readline().rstrip().split())) for _ in range(3))
team_name_1 = sorted(team, key=lambda student: int(student[1]) % 100)
team_name_2 = sorted(team, key=lambda student: -int(student[0]))

for student in team_name_1:
    print(int(student[1]) % 100, end="")
    
print()

for student in team_name_2:
    print(student[2][0], end="")