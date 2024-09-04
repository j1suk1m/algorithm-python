def solution(my_string, is_prefix):
    answer = 1
    
    if len(is_prefix) > len(my_string):
        answer = 0
    else:
        for index in range(len(is_prefix)):
            if my_string[index] != is_prefix[index]:
                answer = 0
                break
        
    return answer