from sys import stdin

test_case = 1 ### 테스트 케이스 번호

while True:
    word = stdin.readline().rstrip()
    alphabets = stdin.readline().rstrip()
    
    if word == "END" and alphabets == "END": ### 종료 조건
        break
    elif len(word) != len(alphabets):
        print("Case {}: different".format(test_case))
    elif sorted(word) != sorted(alphabets):
        print("Case {}: different".format(test_case))
    else:
        print("Case {}: same".format(test_case))
    
    test_case += 1