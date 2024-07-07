from sys import stdin

student_num = 30
student_list = [0] * (student_num + 1)

for _ in range(student_num - 2):
    student_list[int(stdin.readline().rstrip())] = 1

for student in range(1, student_num + 1):
    if (student_list[student] == 0):
        print(student)