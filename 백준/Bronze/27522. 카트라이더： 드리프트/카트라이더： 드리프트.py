from sys import stdin

records = []
scores = [0, 10, 8, 6, 5, 4, 3, 2, 1] ### 순위에 따른 점수
blue_team = 0 
red_team = 0
rank = 1 ### 순위

for _ in range(8):
    time, team = map(str, stdin.readline().rstrip().split())
    m, s, ms = map(int, time.split(':'))
    records.append((m, s, ms, team))
    
records = sorted(records, key=lambda record:(record[0], record[1], record[2]))

for record in records:
    if record[3] == 'R':
        red_team += scores[rank]
    else:
        blue_team += scores[rank]
        
    rank += 1
    
if red_team > blue_team:
    print("Red")
else:
    print("Blue")