from sys import stdin

n = int(stdin.readline().rstrip())
students = list(tuple(map(str, stdin.readline().rstrip().split())) for _ in range(n))
students = sorted(students, key=lambda student: (-int(student[3]), -int(student[2]), -int(student[1])))

print(students[0][0])
print(students[-1][0])