from sys import stdin

n = int(stdin.readline().rstrip())
A = stdin.readline().rstrip().split()
popularity = [0] * n

for _ in range(n):
    for student in stdin.readline().rstrip().split():
        popularity[A.index(student)] += 1
        
students = sorted(list((A[student], popularity[student]) for student in range(n)), key=lambda student: (-student[1], student[0]))

for student in students:
    print(*student)