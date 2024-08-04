from sys import stdin

while True:
    N = int(stdin.readline().rstrip())
    
    if N == 0: ### 종료 조건
        break
    
    students = [] ### (이름, 미터, 센티미터) 리스트
    
    for _ in range(N):
        name, height = map(str, stdin.readline().rstrip().split())
        m, cm = map(int, height.split("."))
        students.append((name, m, cm))
        
    students = sorted(students, key=lambda student:(-student[1], -student[2]))
    highest = (students[0][1], students[0][2]) ### 가장 큰 학생의 키
    
    for student in students: ### 키가 가장 큰 학생들을 모두 출력
        if (student[1], student[2]) == highest:
            print(student[0], end=" ")
        else:
            break
        
    print()