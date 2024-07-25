from sys import stdin

grade_dict = {"A+": 4.5, "A0": 4.0, "B+": 3.5,
              "B0": 3.0, "C+": 2.5, "C0": 2.0,
              "D+": 1.5, "D0": 1.0, "F": 0.0}

total_credits = 0 ### 이수한 총 학점
sum_of_product = 0 ### 과목당 학점 * 등급의 합

for _ in range(20):
    subject, credit, grade = map(str, stdin.readline().rstrip().split())
    
    if grade in grade_dict.keys():
        total_credits += float(credit)
        sum_of_product += (float(credit) * grade_dict[grade])
        
print(sum_of_product / total_credits) 