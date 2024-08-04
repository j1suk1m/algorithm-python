from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
students = [] ### (학생 번호, 총 점수) 리스트
scores = [0] * 101 ### 문제 번호를 인덱스로 하는 배점 리스트
problem = 1 ### 문제 번호

### 각 문제에 할당된 배점 저장
for score in list(map(int, stdin.readline().rstrip().split())):
    scores[problem] = score
    problem += 1
    
for _ in range(M):
    input = stdin.readline().rstrip().split()
    student_number = int(input[0]) ### 학생 번호
    score = 0 ### 학생 점수
    
    ### 맞은 문제에 대한 점수 합산
    for problem in range(1, N + 1):
        if input[problem] == "O":
            score += scores[problem]
            
    students.append((student_number, score))

students = sorted(students, key=lambda student:(-student[1], student[0]))
print(students[0][0], students[0][1])