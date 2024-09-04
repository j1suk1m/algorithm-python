def solution(my_string, is_suffix):
    answer = 1
    
    if len(is_suffix) > len(my_string):
        answer = 0
    else:
        for index in range(-1, -len(is_suffix) - 1, -1):
            if my_string[index] != is_suffix[index]:
                answer = 0
                break
        
    return answer