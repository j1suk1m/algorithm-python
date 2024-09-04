def solution(my_strings, parts):
    answer = ''
    
    for string, part in zip(my_strings, parts):
        start, end = part
        answer += string[start:end + 1]
        
    return answer