from sys import stdin

test_num = int(stdin.readline().rstrip())

for _ in range(test_num):
    test_case = stdin.readline().rstrip()
    correct_num = 0
    score = 0
    
    for result in test_case:
        if (result == 'O'):
            correct_num += 1
            score += correct_num
        else:
            correct_num = 0
       
    print(score)