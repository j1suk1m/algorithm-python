from sys import stdin

input = lambda: stdin.readline().rstrip()

lower_bound = 1
upper_bound = 10

while True:
    question_number = int(input())
    
    ### 종료 조건
    if question_number == 0:
        break

    answer = input()
        
    if answer == "too high":
        upper_bound = min(upper_bound, question_number - 1); ### 상한 갱신
    elif answer == "too low":
        lower_bound = max(lower_bound, question_number + 1); ### 하한 갱신
    else: ### 상한 및 하한이 유효한 범위인지 확인
        if lower_bound <= question_number and question_number <= upper_bound:
            print("Stan may be honest")
        else: 
            print("Stan is dishonest")
        
        ### 다음 게임을 위해 상한 및 하한 초기화
        lower_bound = 1
        upper_bound = 10