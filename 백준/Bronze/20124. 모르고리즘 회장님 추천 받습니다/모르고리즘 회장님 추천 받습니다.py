from sys import stdin

N = int(stdin.readline().rstrip())
records = []

for _ in range(N):
    name, score = map(str, stdin.readline().rstrip().split())
    records.append((name, int(score)))
    
records = sorted(records, key=lambda record: (-record[1], record[0]))
print(records[0][0])
