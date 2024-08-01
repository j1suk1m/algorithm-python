from sys import stdin

N = int(stdin.readline().rstrip())
students = []

for _ in range(N):
    name, korean, english, math = map(str, stdin.readline().rstrip().split())
    students.append((int(korean), int(english), int(math), name))
    
students = sorted(students, key=lambda student: (-student[0], student[1], -student[2], student[3]))

for student in students:
    print(student[3])