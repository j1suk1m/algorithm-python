def solution(num_list):
    answer = -1
    
    for index in range(len(num_list)):
        if num_list[index] < 0:
            answer = index
            break
            
    return answer