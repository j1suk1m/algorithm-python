from sys import stdin

input = lambda: stdin.readline().rstrip()

N = int(input())
students = list(tuple(list(map(int, input().split()))) for _ in range(N))
sorted_students = sorted(students, key=lambda student: -(student[2]))
countries = [0] * (N + 1)
winners = []

for country, student, score in sorted_students:
    if countries[country] < 2:
        countries[country] += 1
        winners.append((country, student))
    if len(winners) == 3:
        break
    
for winner in winners:
    print(*winner)